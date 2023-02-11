import binary
import random

def test_varint():
    x = random.randint(0, 2 ** 64 - 1)
    for i in range(1000):
        data = binary.PutUvarint(x)
        y, _ = binary.ReadUvarint(data)
        assert x == y