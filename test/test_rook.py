import unittest
from juego.rook import Rook
from juego.board import Board
from juego.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):
        board = Board()
        rook = Rook("White", board)
        self.assertEqual(
            str(rook),
            "♜",
        )

    def test_move_vertical_desc(self):
        board = Board()
        rook = Rook("White", board)
        possibles = rook.possible_positions_vertical_down(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )
#Si la torre llega hasta posicion 1,1, no puede seguir a la 0,1.
    def test_move_vertical_asc(self):
        board = Board()
        rook = Rook("White", board)
        possibles = rook.possible_positions_vertical_up(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1)]
        )
#test raro. deberia poder ir a la 6,1 y 7,1??? o esta tomando otras piezas
    def test_move_vertical_desc_with_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("White", board))
        rook = Rook("White", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vertical_down(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):
        board = Board()
        board.set_piece(6, 1, Pawn("Black", board))
        rook = Rook("White", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vertical_down(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )
    
    def test_move_vertical_asc_with_own_piece(self):
        board=Board()
        board.set_piece(2,4,Pawn("White",board))
        rook=Rook("White",board)
        board.set_piece(5,4,rook)
        possibles=rook.possible_positions_vertical_up(5,4)
        self.assertEqual(possibles,[(4,4),(3,4)])
    
    def test_move_vertical_asc_with_not_own_piece(self):
        board=Board()
        board.set_piece(2,4,Pawn("Black",board))
        rook=Rook("White",board)
        board.set_piece(6,4,rook)
        possibles=rook.possible_positions_vertical_up(6,4)
        self.assertEqual(possibles,[(5,4),(4,4),(3,4),(2,4)])
    

if __name__ == '__main__':
    unittest.main()