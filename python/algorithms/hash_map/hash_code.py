def hash_code(s):
    mask = (1 << 32) - 1
    h = 0
    for character in s:
        h = (h << 5 & mask) | (h >> 27)
        h += ord(character)
    print(h)
    return h
hash_code("okay_cool")