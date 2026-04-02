from crypto.hashing import sha256

def build_merkle(leaves):
    if not leaves:
        return None

    nodes = [sha256(str(x)) for x in leaves]

    while len(nodes) > 1:
        temp = []
        for i in range(0, len(nodes), 2):
            left = nodes[i]
            right = nodes[i+1] if i+1 < len(nodes) else left
            temp.append(sha256(left + right))
        nodes = temp

    return nodes[0]