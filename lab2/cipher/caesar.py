ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class CaesarCipher:
    def encrypt(self, text: str, key: int) -> str:
        return self._shift_text(text, key)

    def decrypt(self, text: str, key: int) -> str:
        return self._shift_text(text, -key)

    def _shift_text(self, text: str, key: int) -> str:
        result = []
        for char in text.upper():
            if char in ALPHABET:
                index = ALPHABET.index(char)
                result.append(ALPHABET[(index + key) % len(ALPHABET)])
            else:
                result.append(char)
        return "".join(result)
