import os
import json
import sys

try:
    import psycopg2
    from psycopg2 import extras
    HAS_PSYCOPG2 = True
    print("psycopg2-binary 已成功安装", file=sys.stderr)
    print(f"psycopg2 版本: {psycopg2.__version__}", file=sys.stderr)
except ImportError as e:
    HAS_PSYCOPG2 = False
    print(f"警告: psycopg2-binary 未安装，错误: {e}", file=sys.stderr)
    print("将使用 SQLite", file=sys.stderr)

import sqlite3

DATABASE_URL = os.environ.get('DATABASE_URL')

print(f"DATABASE_URL 环境变量: {'已设置 (长度: ' + str(len(DATABASE_URL)) + ')' if DATABASE_URL else '未设置'}", file=sys.stderr)
if DATABASE_URL:
    print(f"DATABASE_URL 前缀: {DATABASE_URL[:50]}...", file=sys.stderr)

def get_connection():
    if DATABASE_URL and HAS_PSYCOPG2:
        try:
            print("尝试连接 PostgreSQL 数据库...", file=sys.stderr)
            
            import socket
            socket.setdefaulttimeout(10)
            
            dsn_params = {}
            if DATABASE_URL.startswith('postgresql://'):
                url = DATABASE_URL[len('postgresql://'):]
                parts = url.split('@')
                if len(parts) == 2:
                    user_pass, host_port_db = parts
                    up_parts = user_pass.split(':')
                    dsn_params['user'] = up_parts[0]
                    if len(up_parts) > 1:
                        dsn_params['password'] = up_parts[1]
                    
                    host_port_db_parts = host_port_db.split('/')
                    host_port = host_port_db_parts[0]
                    if len(host_port_db_parts) > 1:
                        dsn_params['dbname'] = host_port_db_parts[1]
                    
                    hp_parts = host_port.split(':')
                    original_host = hp_parts[0]
                    if len(hp_parts) > 1:
                        dsn_params['port'] = hp_parts[1]
            
            dsn_params['sslmode'] = 'require'
            
            resolved_host = original_host
            try:
                import socket
                results = socket.getaddrinfo(original_host, 5432, socket.AF_INET, socket.SOCK_STREAM)
                if results:
                    resolved_host = results[0][4][0]
                    print(f"使用 IPv4 地址: {resolved_host}", file=sys.stderr)
            except Exception as e:
                print(f"socket.getaddrinfo 失败: {e}", file=sys.stderr)
            
            if resolved_host == original_host:
                try:
                    import socket as sock_module
                    host_ip = sock_module.gethostbyname(original_host)
                    if ':' not in host_ip:
                        resolved_host = host_ip
                        print(f"使用 gethostbyname 获取的 IPv4 地址: {resolved_host}", file=sys.stderr)
                except Exception as e:
                    print(f"gethostbyname 失败: {e}", file=sys.stderr)
            
            if ':' in resolved_host:
                print(f"警告: 解析到的地址包含冒号，可能是 IPv6: {resolved_host}", file=sys.stderr)
                print("尝试使用备用方法解析...", file=sys.stderr)
                
                try:
                    import subprocess
                    result = subprocess.run(
                        ['getent', 'hosts', original_host],
                        capture_output=True,
                        text=True,
                        timeout=5
                    )
                    if result.returncode == 0:
                        for line in result.stdout.strip().split('\n'):
                            parts = line.split()
                            if parts and ':' not in parts[0]:
                                resolved_host = parts[0]
                                print(f"通过 getent 获取 IPv4 地址: {resolved_host}", file=sys.stderr)
                                break
                except Exception as e:
                    print(f"getent 失败: {e}", file=sys.stderr)
                
                if ':' in resolved_host:
                    try:
                        import dns.resolver
                        answers = dns.resolver.resolve(original_host, 'A')
                        for rdata in answers:
                            resolved_host = str(rdata)
                            print(f"通过 dnspython 获取 IPv4 地址: {resolved_host}", file=sys.stderr)
                            break
                    except Exception as e:
                        print(f"dnspython 失败: {e}", file=sys.stderr)
                
                if ':' in resolved_host:
                    try:
                        import socket
                        import struct
                        resolver = socket.getaddrinfo(original_host, 5432, 0, socket.SOCK_STREAM)
                        for info in resolver:
                            ip = info[4][0]
                            if ':' not in ip:
                                resolved_host = ip
                                print(f"遍历 getaddrinfo 结果找到 IPv4: {resolved_host}", file=sys.stderr)
                                break
                    except Exception as e:
                        print(f"遍历 getaddrinfo 失败: {e}", file=sys.stderr)
                
                if ':' in resolved_host:
                    try:
                        import urllib.request
                        import json
                        url = f"https://cloudflare-dns.com/dns-query?name={original_host}&type=A"
                        headers = {'accept': 'application/dns-json'}
                        req = urllib.request.Request(url, headers=headers)
                        with urllib.request.urlopen(req, timeout=5) as response:
                            data = json.loads(response.read().decode())
                            if 'Answer' in data:
                                for answer in data['Answer']:
                                    if answer['type'] == 1:
                                        resolved_host = answer['data']
                                        print(f"通过 Cloudflare DNS 获取 IPv4 地址: {resolved_host}", file=sys.stderr)
                                        break
                    except Exception as e:
                        print(f"Cloudflare DNS 查询失败: {e}", file=sys.stderr)
            
            dsn_params['host'] = resolved_host
            
            print(f"PostgreSQL 连接参数: host={dsn_params.get('host')}, port={dsn_params.get('port')}, dbname={dsn_params.get('dbname')}", file=sys.stderr)
            
            conn = psycopg2.connect(**dsn_params)
            print("成功连接到 PostgreSQL 数据库", file=sys.stderr)
            return conn, True
        except psycopg2.OperationalError as e:
            print(f"PostgreSQL 连接失败 (OperationalError): {e}", file=sys.stderr)
            print("回退到 SQLite", file=sys.stderr)
        except Exception as e:
            print(f"PostgreSQL 连接失败 (其他错误): {type(e).__name__}: {e}", file=sys.stderr)
            print("回退到 SQLite", file=sys.stderr)
    
    db_path = os.environ.get('DATABASE_PATH', os.path.join(os.path.dirname(__file__), 'game.db'))
    print(f"使用 SQLite 数据库: {db_path}", file=sys.stderr)
    return sqlite3.connect(db_path), False

def init_db():
    try:
        conn, is_postgresql = get_connection()
        
        if is_postgresql:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    id SERIAL PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            cur.close()
        else:
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    data TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            c.close()
        
        conn.close()
        print(f"数据库初始化成功 (PostgreSQL: {is_postgresql})", file=sys.stderr)
        return True, is_postgresql
    except Exception as e:
        print(f"数据库初始化失败: {e}", file=sys.stderr)
        return False, False

def save_player(name, data):
    conn, is_postgresql = get_connection()
    
    data_json = json.dumps(data, ensure_ascii=False)
    
    if is_postgresql:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO players (name, data, updated_at)
            VALUES (%s, %s, CURRENT_TIMESTAMP)
            ON CONFLICT (name) DO UPDATE SET data = %s, updated_at = CURRENT_TIMESTAMP
        ''', (name, data_json, data_json))
        conn.commit()
        cur.close()
    else:
        c = conn.cursor()
        c.execute('''
            INSERT OR REPLACE INTO players (name, data, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        ''', (name, data_json))
        conn.commit()
        c.close()
    
    conn.close()

def load_player(name):
    conn, is_postgresql = get_connection()
    
    if is_postgresql:
        cur = conn.cursor()
        cur.execute('SELECT data FROM players WHERE name = %s', (name,))
        row = cur.fetchone()
        cur.close()
    else:
        c = conn.cursor()
        c.execute('SELECT data FROM players WHERE name = ?', (name,))
        row = c.fetchone()
        c.close()
    
    conn.close()
    
    if row:
        return json.loads(row[0])
    return None

def delete_player(name):
    conn, is_postgresql = get_connection()
    
    if is_postgresql:
        cur = conn.cursor()
        cur.execute('DELETE FROM players WHERE name = %s', (name,))
        affected = cur.rowcount
        conn.commit()
        cur.close()
    else:
        c = conn.cursor()
        c.execute('DELETE FROM players WHERE name = ?', (name,))
        affected = c.rowcount
        conn.commit()
        c.close()
    
    conn.close()
    
    return affected > 0

def player_exists(name):
    conn, is_postgresql = get_connection()
    
    if is_postgresql:
        cur = conn.cursor()
        cur.execute('SELECT 1 FROM players WHERE name = %s', (name,))
        exists = cur.fetchone() is not None
        cur.close()
    else:
        c = conn.cursor()
        c.execute('SELECT 1 FROM players WHERE name = ?', (name,))
        exists = c.fetchone() is not None
        c.close()
    
    conn.close()
    
    return exists

def get_all_players():
    conn, is_postgresql = get_connection()
    
    if is_postgresql:
        cur = conn.cursor()
        cur.execute('SELECT name, data FROM players ORDER BY updated_at DESC')
        rows = cur.fetchall()
        cur.close()
    else:
        c = conn.cursor()
        c.execute('SELECT name, data FROM players ORDER BY updated_at DESC')
        rows = c.fetchall()
        c.close()
    
    conn.close()
    
    players = []
    for row in rows:
        try:
            data = json.loads(row[1])
            players.append({
                'name': row[0],
                'level': data.get('player', {}).get('level', 1),
                'region': data.get('current_region', 'region_1'),
                'gold': data.get('player', {}).get('gold', 0)
            })
        except:
            pass
    
    return players

init_db()
