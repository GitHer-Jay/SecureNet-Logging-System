import hashlib

def generate_hash(data, prev_hash):
    combined = str(data) + str(prev_hash)
    return hashlib.sha256(combined.encode()).hexdigest()