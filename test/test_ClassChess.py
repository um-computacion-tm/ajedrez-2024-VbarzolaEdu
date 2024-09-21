from juego.chess import Chess
from juego.board import Board
from juego.rook import Rook
from juego.bishop import Bishop
from juego.knight import Knight
from juego.pawn import Pawn
from juego.exceptions import *
import unittest

class TestChess(unittest.TestCase):

#testeamos que las piezas se muevan bien y que el espacio que queda es un espacio vacio
    def setUp(self):
        self.chess = Chess()

    def test_valid_move(self):
        self.chess.move(6, 0, 4, 0)  # Mover peón blanco de (6, 0) a (4, 0)
        board = self.chess.__board__  # Acceder al tablero
        self.assertIsNone(board.__positions__[6][0])  # La posición de origen debe estar vacía
        self.assertIsNotNone(board.__positions__[4][0])  # La posición de destino debe contener la pieza

    def test_invalid_turn(self):
        self.chess.move(6, 0, 4, 0)  # Mover peón blanco de (6, 0) a (4, 0)
        with self.assertRaises(InvalidTurn):
            self.chess.move(6, 1, 4, 1)  # Intentar mover otro peón blanco fuera de turno

    def test_destination_invalid_move(self):
        with self.assertRaises(DestinationInvalidMove):
            self.chess.move(6, 0, 8, 0)  # Mover peón blanco fuera del tablero
    
    def test_invalid_move(self):
        with self.assertRaises(InvalidMove):
            self.chess.move(6, 0, 5, 1)  # Movimiento inválido para un peón blanco
    

if __name__== "__main__" :
    unittest.main()

