ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class VigenereCipher:
    def encrypt(self, text: str, key: str) -> str:
        return self._transform(text, key, decrypt=False)

    def decrypt(self, text: str, key: str) -> str:
        return self._transform(text, key, decrypt=True)

    def _transform(self, text: str, key: str, decrypt: bool) -> str:
        cleaned_key = "".join(char for char in key.upper() if char in ALPHABET)
        if not cleaned_key:
            raise ValueError("Key must contain at least one alphabetic character.")

        result = []
        key_index = 0
        for char in text.upper():
            if char in ALPHABET:
                shift = ALPHABET.index(cleaned_key[key_index % len(cleaned_key)])
                if decrypt:
                    shift = -shift
                char_index = ALPHABET.index(char)
                result.append(ALPHABET[(char_index + shift) % len(ALPHABET)])
                key_index += 1
            else:
                result.append(char)
        return "".join(result)
