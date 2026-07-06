import sqlite3
import os
import json

DB_PATH = os.environ.get('DATABASE_PATH', os.path.join(os.path.dirname(__file__), 'game.db'))

def init_db():
    conn = sqlite3.connect(DB_PATH)
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
    conn.close()

def save_player(name, data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    data_json = json.dumps(data, ensure_ascii=False)
    
    c.execute('''
        INSERT OR REPLACE INTO players (name, data, updated_at)
        VALUES (?, ?, CURRENT_TIMESTAMP)
    ''', (name, data_json))
    
    conn.commit()
    conn.close()

def load_player(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT data FROM players WHERE name = ?', (name,))
    row = c.fetchone()
    
    conn.close()
    
    if row:
        return json.loads(row[0])
    return None

def delete_player(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('DELETE FROM players WHERE name = ?', (name,))
    affected = c.rowcount
    
    conn.commit()
    conn.close()
    
    return affected > 0

def player_exists(name):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT 1 FROM players WHERE name = ?', (name,))
    exists = c.fetchone() is not None
    
    conn.close()
    
    return exists

def get_all_players():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT name, data FROM players ORDER BY updated_at DESC')
    rows = c.fetchall()
    
    conn.close()
    
    players = []
    for row in rows:
        try:
            data = json.loads(row[1])
            players.append({
                'name': row[0],
                'level': data.get('level', 1),
                'region': data.get('region', 'day1'),
                'gold': data.get('gold', 0)
            })
        except:
            pass
    
    return players

init_db()
