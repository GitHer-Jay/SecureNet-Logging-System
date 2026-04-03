import psycopg2
from config import DB_CONFIG

def connect():
    return psycopg2.connect(**DB_CONFIG)

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id SERIAL PRIMARY KEY,
        event TEXT,
        description TEXT,
        user_id TEXT,
        ip_address TEXT,
        prev_hash TEXT,
        current_hash TEXT
    )
    """)

    conn.commit()
    conn.close()