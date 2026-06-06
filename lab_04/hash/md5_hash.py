import hashlib
import struct
import math


class MD5Hash:
    """Custom MD5 implementation for educational purposes."""
    
    def __init__(self):
        # Initial MD5 constants
        self.A = 0x67452301
        self.B = 0xEFCDAB89
        self.C = 0x98BADCFE
        self.D = 0x10325476

        # Sine-derived constants
        self.K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

        # Shift amounts
        self.S = [7, 12, 17, 22] * 4 + [5, 9, 14, 20] * 4 + [4, 11, 16, 23] * 4 + [6, 10, 15, 21] * 4

    def _left_rotate(self, x, c):
        return ((x << c) | (x >> (32 - c))) & 0xFFFFFFFF

    def _process_chunk(self, chunk):
        a, b, c, d = self.A, self.B, self.C, self.D

        for i in range(64):
            if i < 16:
                f = (b & c) | ((~b) & d)
                g = i
            elif i < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * i) % 16

            temp = d
            d = c
            c = b
            b = (b + self._left_rotate((a + f + self.K[i] + struct.unpack('<I', chunk[g*4:g*4+4])[0]) & 0xFFFFFFFF, self.S[i])) & 0xFFFFFFFF
            a = temp

        self.A = (self.A + a) & 0xFFFFFFFF
        self.B = (self.B + b) & 0xFFFFFFFF
        self.C = (self.C + c) & 0xFFFFFFFF
        self.D = (self.D + d) & 0xFFFFFFFF

    def hash(self, message: str) -> str:
        message_bytes = bytearray(message.encode())
        original_len_bits = (8 * len(message_bytes)) & 0xFFFFFFFFFFFFFFFF

        # Padding
        message_bytes.append(0x80)
        while (len(message_bytes) * 8) % 512 != 448:
            message_bytes.append(0x00)

        message_bytes += struct.pack('<Q', original_len_bits)

        # Process each 512-bit chunk
        for i in range(0, len(message_bytes), 64):
            self._process_chunk(message_bytes[i:i+64])

        # Output
        return struct.pack('<4I', self.A, self.B, self.C, self.D).hex()


if __name__ == "__main__":
    md5 = MD5Hash()
    test_msg = "Hello, MD5!"
    print(f"Message: {test_msg}")
    print(f"Custom MD5: {md5.hash(test_msg)}")
    print(f"Library MD5: {hashlib.md5(test_msg.encode()).hexdigest()}")
