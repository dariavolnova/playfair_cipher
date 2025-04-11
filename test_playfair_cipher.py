import unittest
from playfair_cipher import PlayfairCipher

class TestPlayfairCipher(unittest.TestCase):

    def setUp(self):
        self.cipher = PlayfairCipher("MONARCHY")

    def test_key_square(self):
        expected = [
            ['M', 'O', 'N', 'A', 'R'],
            ['C', 'H', 'Y', 'B', 'D'],
            ['E', 'F', 'G', 'I', 'K'],
            ['L', 'P', 'Q', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Z']
        ]
        self.assertEqual(self.cipher.key_square, expected)

    def test_encrypt(self):
        encrypted = self.cipher.encrypt("INSTRUMENTS")
        self.assertEqual(encrypted, "GATLMZCLRQXA")

    def test_repeating_letters(self):
        encrypted = self.cipher.encrypt("BALLOON")
        self.assertEqual(encrypted, "IBSUPMNA")

    def test_odd_length_input(self):
        encrypted = self.cipher.encrypt("HELLO")
        self.assertEqual(encrypted, "CFSUPM")

    def test_decrypt(self):
        decrypted = self.cipher.decrypt("GATLMZCLRQXA")
        self.assertEqual(decrypted, "INSTRUMENTSX")


if __name__ == "__main__":
    unittest.main()
