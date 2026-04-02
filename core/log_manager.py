from datetime import datetime
from core.database import connect
from core.hash_chain import generate_hash
from core.merkle_tree import build_merkle


def add_log(event, desc, user, ip):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM logs ORDER BY id DESC LIMIT 1")
    last = cur.fetchone()

    index = last[0] + 1 if last else 0
    prev_hash = last[7] if last else "0"

    timestamp = str(datetime.now())

    curr_hash = generate_hash(index, timestamp, event, desc, user, ip, prev_hash)

    # Build Merkle tree
    cur.execute("SELECT curr_hash FROM logs")
    rows = cur.fetchall()

    leaves = [r[0] for r in rows]
    leaves.append(curr_hash)

    merkle_root = build_merkle(leaves)

    cur.execute("""
    INSERT INTO logs (timestamp, event, description, user_name, ip, prev_hash, curr_hash, merkle_root)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """, (timestamp, event, desc, user, ip, prev_hash, curr_hash, merkle_root))

    conn.commit()
    conn.close()

    return merkle_root