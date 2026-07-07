import os
import json
import sys

try:
    import psycopg2
    from psycopg2 import extras
    HAS_PSYCOPG2 = True
    print("psycopg2-binary 已成功安装", file=sys.stderr)
except ImportError:
    HAS_PSYCOPG2 = False
    print("警告: psycopg2-binary 未安装，将使用 SQLite", file=sys.stderr)

import sqlite3

DATABASE_URL = os.environ.get('DATABASE_URL')

print(f"DATABASE_URL 环境变量: {'已设置 (长度: ' + str(len(DATABASE_URL)) + ')' if DATABASE_URL else '未设置'}", file=sys.stderr)

def is_using_postgresql():
    return DATABASE_URL and HAS_PSYCOPG2

def get_connection():
    if is_using_postgresql():
        try:
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            print("成功连接到 PostgreSQL 数据库", file=sys.stderr)
            return conn
        except Exception as e:
            print(f"PostgreSQL 连接失败: {e}", file=sys.stderr)
            print("回退到 SQLite", file=sys.stderr)
    
    db_path = os.environ.get('DATABASE_PATH', os.path.join(os.path.dirname(__file__), 'game.db'))
    print(f"使用 SQLite 数据库: {db_path}", file=sys.stderr)
    return sqlite3.connect(db_path)

def init_db():
    try:
        conn = get_connection()
        
        if is_using_postgresql():
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
        print(f"数据库初始化成功 (PostgreSQL: {is_using_postgresql()})", file=sys.stderr)
        return True
    except Exception as e:
        print(f"数据库初始化失败: {e}", file=sys.stderr)
        return False

def save_player(name, data):
    conn = get_connection()
    
    data_json = json.dumps(data, ensure_ascii=False)
    
    if is_using_postgresql():
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
    conn = get_connection()
    
    if is_using_postgresql():
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
    conn = get_connection()
    
    if is_using_postgresql():
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
    conn = get_connection()
    
    if is_using_postgresql():
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
    conn = get_connection()
    
    if is_using_postgresql():
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
