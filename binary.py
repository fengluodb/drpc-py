MaxVarintLen64 = 10


def PutUvarint(x: int) -> bytes:
    buf = []
    while x >= 0x80:
      buf.append(x & 0x7f | 0x80)
      x >>= 7
    buf.append(x)
    return bytes(buf)

def ReadUvarint(data: bytes) -> tuple[int, int]:
    x = 0
    s = 0
    for i, b in enumerate(data):
        if i == MaxVarintLen64:
            return 0, -(i + 1) # overflow

        if b < 0x80:
            if i == MaxVarintLen64-1 and b > 1:
                return 0, -(i + 1) # overflow
            return x | b << s, i + 1
        
        x |= (b & 0x7f) << s
        s += 7

    return 0, 0
