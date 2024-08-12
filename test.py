import unittest
from main import chess

class Testa(unittest.TestCase):
    def testa(self):
        self.assertEqual(chess(), "Juego del Ajedrez")

if __name__ == '__main__':
    unittest.main()