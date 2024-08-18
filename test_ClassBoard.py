from ClassBoard import Board
from ClassRook import Rook
from ClassHorse import Horse
from ClassBishop import Bishop
from ClassQueen import Queen
from ClassKing import King
from ClassPawn import Pawn
from ClassPiece import Piece

import unittest

#test para saber si la posicion de la pieza es correcta al inicio del juego.
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=Board()
    #para las negras
    def test_get_piece(self):
        self.assertIsInstance(self.board.get_piece(0,0), Rook)
        self.assertIsInstance(self.board.get_piece(0,1), Horse)
        self.assertIsInstance(self.board.get_piece(0,2), Bishop)
        self.assertIsInstance(self.board.get_piece(0,3), Queen)
        self.assertIsInstance(self.board.get_piece(0,4), King)
        self.assertIsInstance(self.board.get_piece(0,5), Bishop)
        self.assertIsInstance(self.board.get_piece(0,6), Horse)
        self.assertIsInstance(self.board.get_piece(0,7), Rook)
       
        for i in range (8):
            piece= self.board.get_piece(1,i)
            self.assertIsInstance(piece, Pawn)
        #para blancas
        self.assertIsInstance(self.board.get_piece(7,0), Rook)
        self.assertIsInstance(self.board.get_piece(7,1), Horse)
        self.assertIsInstance(self.board.get_piece(7,2), Bishop)
        self.assertIsInstance(self.board.get_piece(7,3), Queen)
        self.assertIsInstance(self.board.get_piece(7,4), King)
        self.assertIsInstance(self.board.get_piece(7,5), Bishop)
        self.assertIsInstance(self.board.get_piece(7,6), Horse)
        self.assertIsInstance(self.board.get_piece(7,7), Rook)
        for i in range (8):
            piece= self.board.get_piece(6,i)
            self.assertIsInstance(piece, Pawn)
            #para posiciones que esten vacias en el inicio
        for i in range(2,6):
            for j in range(8):
                self.assertIsNone(self.board.get_piece(i,j))


if __name__ == '__main__':
    unittest.main()