from core.database import connect

def get_logs():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id, event, user_id, ip_address FROM logs ORDER BY id ASC")
    rows = cur.fetchall()

    logs = []
    for row in rows:
        logs.append({
            "id": row[0],
            "event": row[1],
            "user": row[2],
            "ip": row[3]
        })

    conn.close()
    return logs