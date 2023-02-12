import binary

from struct import *

class RequestHeader():
    def __init__(self, id: int, method: str, checksum: int):
        self.id = id
        self.method = method
        self.checksum = checksum
        self.data = []

    def marshal(self) -> bytes:
        data = binary.PutUvarint(self.id)
        data += binary.write_string(self.method)
        data += bytearray(pack('@I', self.checksum))
        return data

    def unmarshal(self, data:bytes) -> None:
        idx = 0
        data = bytearray(data)

        self.id, size = binary.ReadUvarint(data)
        idx += size
        self.method, size = binary.read_string(data[idx:])
        idx += size
        self.checksum = unpack('@I', bytes(data[idx:]))[0]


class ResponseHeader():
    def __init__(self, id: int, error: str, checksum: int):
        self.id = id
        self.error = error
        self.checksum = checksum
        self.data = []

    def marshal(self) -> bytes:
        data = binary.PutUvarint(self.id)
        data += binary.write_string(self.error)
        data += bytearray(pack('@I', self.checksum))
        return data

    def unmarshal(self, data:bytes) -> None:
        idx = 0
        data = bytearray(data)

        self.id, size = binary.ReadUvarint(data)
        idx += size
        self.error, size = binary.read_string(data[idx:])
        idx += size
        self.checksum = unpack('@I', bytes(data[idx:]))[0]