from core.database import connect
from core.hash_chain import generate_hash

def verify_logs():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id, event, description, user_id, ip_address, prev_hash, current_hash FROM logs ORDER BY id")
    rows = cur.fetchall()

    prev_hash = "0"

    for row in rows:
        id, event, desc, user, ip, db_prev, db_hash = row

        if db_prev != prev_hash:
            return f"❌ Tampered at log {id} (prev hash mismatch)"

        data = f"{event}{desc}{user}{ip}"
        calc_hash = generate_hash(data, prev_hash)

        if calc_hash != db_hash:
            return f"❌ Tampered at log {id} (hash mismatch)"

        prev_hash = db_hash

    return "✅ Logs are secure"