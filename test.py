import binary
import random
import string
import header

def generate_random_string() -> str:
    n = random.randint(0, 10000)
    s = ''
    for _ in range(n):
        s += random.choice(string.printable)
    return s

def test_varint():
    x = random.randint(0, 2 ** 64 - 1)
    for _ in range(1000):
        data = binary.PutUvarint(x)
        y, _ = binary.ReadUvarint(data)
        assert x == y

def test_string():
    for _ in range(1000):
        s = generate_random_string()
        data = binary.write_string(s)
        new_s, _ = binary.read_string(data)
        assert new_s == s

def test_RequestHeader():
    for _ in range(1000):
        id = random.randint(0, 2 ** 64 - 1)
        method = generate_random_string()
        checksum = random.randint(0, 2 ** 32 - 1)
        old_req = header.RequestHeader(id, method, checksum)
        new_req = header.RequestHeader(0, '', 0)

        data = old_req.marshal()
        new_req.unmarshal(data)

        assert old_req.id == new_req.id
        assert old_req.method == new_req.method
        assert old_req.checksum == new_req.checksum


def test_ResponseHeader():
    for _ in range(1000):
        id = random.randint(0, 2 ** 64 - 1)
        error = generate_random_string()
        checksum = random.randint(0, 2 ** 32 - 1)
        old_resp = header.ResponseHeader(id, error, checksum)
        new_resp = header.ResponseHeader(0, '', 0)

        data = old_resp.marshal()
        new_resp.unmarshal(data)

        assert old_resp.id == new_resp.id
        assert old_resp.error == new_resp.error
        assert old_resp.checksum == new_resp.checksum