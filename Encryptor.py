

class Encryptor:
    def __init__(self, key: int):
        self.key = key

    def xor_encrypt(self, data: str) -> str:
        return ''.join(chr(ord(c) ^ self.key) for c in data)

    def xor_decrypt(self, data: str) -> str:
        return ''.join(chr(ord(c) ^ self.key) for c in data)
