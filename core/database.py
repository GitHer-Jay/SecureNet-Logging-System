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
        timestamp TEXT,
        event TEXT,
        description TEXT,
        user_name TEXT,
        ip TEXT,
        prev_hash TEXT,
        curr_hash TEXT,
        merkle_root TEXT
    )
    """)

    conn.commit()
    conn.close()