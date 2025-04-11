import string

class PlayfairCipher:
    def __init__(self, key: str):
        self.key_square = self.generate_key_square(key)

    def generate_key_square(self, key: str):
        key = key.upper().replace("J", "I")
        seen = set()
        filtered_key = []

        for char in key:
            if char in string.ascii_uppercase and char not in seen:
                seen.add(char)
                filtered_key.append(char)

        for char in string.ascii_uppercase:
            if char == 'J':
                continue
            if char not in seen:
                filtered_key.append(char)

        square = [filtered_key[i:i+5] for i in range(0, 25, 5)]
        return square

    def find_position(self, char):
        for row in range(5):
            for col in range(5):
                if self.key_square[row][col] == char:
                    return row, col
        raise ValueError(f"Character {char} not found in key square")

    def preprocess_text(self, text: str):
        text = text.upper().replace("J", "I")
        text = ''.join(filter(str.isalpha, text))

        i = 0
        result = []
        while i < len(text):
            a = text[i]
            b = text[i+1] if i + 1 < len(text) else 'X'
            if a == b:
                result.append(a + 'X')
                i += 1
            else:
                result.append(a + b)
                i += 2

        if len(result[-1]) == 1:
            result[-1] += 'X'

        return result

    def encrypt_pair(self, a, b):
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)

        if row1 == row2:
            return self.key_square[row1][(col1 + 1) % 5] + self.key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            return self.key_square[(row1 + 1) % 5][col1] + self.key_square[(row2 + 1) % 5][col2]
        else:
            return self.key_square[row1][col2] + self.key_square[row2][col1]

    def encrypt(self, plaintext: str) -> str:
        digraphs = self.preprocess_text(plaintext)
        return ''.join(self.encrypt_pair(a, b) for a, b in digraphs)

    def decrypt_pair(self, a, b):
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)

        if row1 == row2:
            return self.key_square[row1][(col1 - 1) % 5] + self.key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            return self.key_square[(row1 - 1) % 5][col1] + self.key_square[(row2 - 1) % 5][col2]
        else:
            return self.key_square[row1][col2] + self.key_square[row2][col1]

    def decrypt(self, ciphertext: str) -> str:
        ciphertext = ciphertext.upper().replace("J", "I")
        ciphertext = ''.join(filter(str.isalpha, ciphertext))

        digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        return ''.join(self.decrypt_pair(a, b) for a, b in digraphs)
