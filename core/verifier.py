from core.database import connect
from core.hash_chain import generate_hash

def verify_logs():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM logs ORDER BY id")
    rows = cur.fetchall()

    if len(rows) <= 1:
        return "⚠️ Not enough logs to verify"

    for i in range(1, len(rows)):
        prev = rows[i-1]
        curr = rows[i]

        # 🔴 Detect deletion
        if curr[0] != prev[0] + 1:
            return f"❌ Log deleted near index {i}"

        # 🔴 Detect chain break
        if curr[6] != prev[7]:
            return f"❌ Chain broken at index {i}"

        # 🔴 Recalculate hash
        recalculated = generate_hash(
            curr[0],
            curr[1],
            curr[2],
            curr[3],
            curr[4],
            curr[5],
            curr[6]
        )

        # 🔴 Detect modification
        if curr[7] != recalculated:
            return f"❌ Data tampered at index {i}"

    return "✅ Logs are secure"