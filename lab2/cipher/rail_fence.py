class RailFenceCipher:
    def encrypt(self, text: str, key: int) -> str:
        if key < 2:
            raise ValueError("Key must be at least 2 for Rail Fence cipher.")

        rails = ["" for _ in range(key)]
        rail = 0
        direction = 1

        for char in text:
            rails[rail] += char
            if rail == 0:
                direction = 1
            elif rail == key - 1:
                direction = -1
            rail += direction

        return "".join(rails)

    def decrypt(self, cipher_text: str, key: int) -> str:
        if key < 2:
            raise ValueError("Key must be at least 2 for Rail Fence cipher.")

        pattern = []
        rail = 0
        direction = 1
        for _ in cipher_text:
            pattern.append(rail)
            if rail == 0:
                direction = 1
            elif rail == key - 1:
                direction = -1
            rail += direction

        rail_lengths = [pattern.count(index) for index in range(key)]
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start : start + length]))
            start += length

        result = []
        for rail_index in pattern:
            result.append(rails[rail_index].pop(0))
        return "".join(result)
