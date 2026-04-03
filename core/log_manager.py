from core.database import connect
from core.hash_chain import generate_hash
from core.merkle_tree import build_merkle_root

def add_log(event, description, user, ip):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT current_hash FROM logs ORDER BY id DESC LIMIT 1")
    prev = cur.fetchone()
    prev_hash = prev[0] if prev else "0"

    data = f"{event}{description}{user}{ip}"
    current_hash = generate_hash(data, prev_hash)

    cur.execute("""
        INSERT INTO logs (event, description, user_id, ip_address, prev_hash, current_hash)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (event, description, user, ip, prev_hash, current_hash))

    conn.commit()

    cur.execute("SELECT current_hash FROM logs")
    hashes = [row[0] for row in cur.fetchall()]

    root = build_merkle_root(hashes)

    conn.close()
    return root