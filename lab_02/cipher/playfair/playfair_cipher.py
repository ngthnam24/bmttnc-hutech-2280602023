ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


class PlayFairCipher:
    def create_playfair_matrix(self, key: str) -> list[list[str]]:
        key = self._normalize_text(key)
        used = []
        for char in key + ALPHABET:
            if char not in used:
                used.append(char)
        return [used[index:index + 5] for index in range(0, 25, 5)]

    def playfair_encrypt(self, plain_text: str, matrix: list[list[str]]) -> str:
        pairs = self._prepare_pairs(plain_text)
        encrypted_text = []
        for pair in pairs:
            row1, col1 = self._find_position(pair[0], matrix)
            row2, col2 = self._find_position(pair[1], matrix)
            if row1 == row2:
                encrypted_text.append(matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5])
            elif col1 == col2:
                encrypted_text.append(matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2])
            else:
                encrypted_text.append(matrix[row1][col2] + matrix[row2][col1])
        return "".join(encrypted_text)

    def playfair_decrypt(self, cipher_text: str, matrix: list[list[str]]) -> str:
        cipher_text = self._normalize_text(cipher_text)
        pairs = [cipher_text[index:index + 2] for index in range(0, len(cipher_text), 2)]
        decrypted_text = []
        for pair in pairs:
            row1, col1 = self._find_position(pair[0], matrix)
            row2, col2 = self._find_position(pair[1], matrix)
            if row1 == row2:
                decrypted_text.append(matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5])
            elif col1 == col2:
                decrypted_text.append(matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2])
            else:
                decrypted_text.append(matrix[row1][col2] + matrix[row2][col1])
        return "".join(decrypted_text)

    def _normalize_text(self, text: str) -> str:
        return "".join("I" if char == "J" else char for char in text.upper() if char.isalpha())

    def _prepare_pairs(self, text: str) -> list[str]:
        text = self._normalize_text(text)
        pairs = []
        index = 0
        while index < len(text):
            first = text[index]
            if index + 1 < len(text):
                second = text[index + 1]
                if first == second:
                    pairs.append(first + "X")
                    index += 1
                else:
                    pairs.append(first + second)
                    index += 2
            else:
                pairs.append(first + "X")
                index += 1
        return pairs

    def _find_position(self, char: str, matrix: list[list[str]]) -> tuple[int, int]:
        for row_index, row in enumerate(matrix):
            if char in row:
                return row_index, row.index(char)
        raise ValueError("Character not found.")
