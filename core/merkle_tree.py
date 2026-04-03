import hashlib

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def build_merkle_root(hashes):
    if not hashes:
        return None

    while len(hashes) > 1:
        temp = []
        for i in range(0, len(hashes), 2):
            left = hashes[i]
            right = hashes[i+1] if i+1 < len(hashes) else left
            temp.append(hash_data(left + right))
        hashes = temp

    return hashes[0]