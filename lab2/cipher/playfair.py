ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


class PlayfairCipher:
    def encrypt(self, plain_text: str, key: str) -> str:
        matrix = self._build_matrix(key)
        pairs = self._prepare_pairs(plain_text)
        return "".join(self._encrypt_pair(pair, matrix) for pair in pairs)

    def decrypt(self, cipher_text: str, key: str) -> str:
        matrix = self._build_matrix(key)
        text = self._normalize_text(cipher_text)
        if len(text) % 2 != 0:
            raise ValueError("Cipher text length must be even for Playfair cipher.")
        pairs = [text[index : index + 2] for index in range(0, len(text), 2)]
        return "".join(self._decrypt_pair(pair, matrix) for pair in pairs)

    def _normalize_text(self, text: str) -> str:
        cleaned = []
        for char in text.upper():
            if char.isalpha():
                cleaned.append("I" if char == "J" else char)
        return "".join(cleaned)

    def _build_matrix(self, key: str) -> list[list[str]]:
        seen = set()
        sequence = []
        for char in self._normalize_text(key) + ALPHABET:
            if char not in seen:
                seen.add(char)
                sequence.append(char)
        return [sequence[index : index + 5] for index in range(0, 25, 5)]

    def _prepare_pairs(self, text: str) -> list[str]:
        normalized = self._normalize_text(text)
        pairs = []
        index = 0
        while index < len(normalized):
            first = normalized[index]
            if index + 1 < len(normalized):
                second = normalized[index + 1]
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
        raise ValueError(f"Character {char} not found in Playfair matrix.")

    def _encrypt_pair(self, pair: str, matrix: list[list[str]]) -> str:
        row1, col1 = self._find_position(pair[0], matrix)
        row2, col2 = self._find_position(pair[1], matrix)

        if row1 == row2:
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        if col1 == col2:
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        return matrix[row1][col2] + matrix[row2][col1]

    def _decrypt_pair(self, pair: str, matrix: list[list[str]]) -> str:
        row1, col1 = self._find_position(pair[0], matrix)
        row2, col2 = self._find_position(pair[1], matrix)

        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        if col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        return matrix[row1][col2] + matrix[row2][col1]
