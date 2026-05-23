import math


class TranspositionCipher:
    def encrypt(self, plain_text: str, key: int) -> str:
        columns = [""] * key
        for column in range(key):
            pointer = column
            while pointer < len(plain_text):
                columns[column] += plain_text[pointer]
                pointer += key
        return "".join(columns)

    def decrypt(self, cipher_text: str, key: int) -> str:
        num_columns = math.ceil(len(cipher_text) / key)
        num_rows = key
        num_shaded_boxes = (num_columns * num_rows) - len(cipher_text)

        plaintext_columns = [""] * num_columns
        column = 0
        row = 0

        for symbol in cipher_text:
            plaintext_columns[column] += symbol
            column += 1
            if column == num_columns or (column == num_columns - 1 and row >= num_rows - num_shaded_boxes):
                column = 0
                row += 1

        return "".join(plaintext_columns)
