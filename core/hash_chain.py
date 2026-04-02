from crypto.hashing import sha256

def generate_hash(index, timestamp, event, desc, user, ip, prev_hash):
    data = f"{index}{timestamp}{event}{desc}{user}{ip}{prev_hash}"
    return sha256(data)