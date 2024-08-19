from juego.ClassChess import Chess
from juego.ClassBoard import Board
from juego.ClassRook import Rook
from juego.ClassBishop import Bishop
from juego.ClassHorse import Horse
import unittest

class TestChess(unittest.TestCase):
#instancio las clases
    def setUp(self):
        self.chess = Chess()
        self.Board = self.chess.__board__

#testeamos que las piezas se muevan bien y que el espacio que queda es un espacio vacio
    def test_move(self):
        self.chess.move(0,0,2,0)
        self.assertIsInstance(self.Board.get_piece(2, 0), Rook)
        self.assertIsNone(self.Board.get_piece(0, 0))
        self.assertEqual(self.chess.turn, "Black")

    




        

if __name__== "__main__" :
    unittest.main()

