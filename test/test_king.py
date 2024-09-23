import unittest
from juego.board import Board
from juego.pawn import Pawn
from juego.king import King


class TestKing(unittest.TestCase):
    
    def test_possible_positions_vertical_down(self):
        board=Board(for_test=True)
        king=King("Black",board)
        possibles=king.possible_positions_vertical(4,1,1,1,6)
        self.assertEqual(possibles,[(5,1)])

    def test_possible_vertical_up(self):
        board=Board(for_test=True)
        king=King("White",board)
        possibles=king.possible_positions_vertical(4,1,-1,-1,2)
        self.assertEqual(possibles,[(3,1)])

    def test_possible_positions_horizontal_right(self):
        board=Board(for_test=True)
        king=King("Black",board)
        possibles=king.possible_positions_horizontal(1,4,1,6,1)
        self.assertEqual(possibles,[(1,5)])

    def test_possible_positions_horizontal_left(self):
        board=Board(for_test=True)
        king=King("White",board)
        possibles=king.possible_positions_horizontal(1,4,-1,2,-1)
        self.assertEqual(possibles,[(1,3)])

    # def test_possible_positions_diagonal_down_right(self):
    #     board=Board(for_test=True)
    #     king=King("Black",board)
    #     possibles=king.possible_positions_diagonal_down_right(1,1)
    #     self.assertEqual(possibles,[(2,2)])
        
    # def test_possible_positions_diagonal_down_left(self):
    #     board=Board(for_test=True)
    #     king=King("White",board)
    #     possibles=king.possible_positions_diagonal_down_left(1,1)
    #     self.assertEqual(possibles,[(2,0)])

    # def test_possible_positions_diagonal_up_right(self):
    #     board=Board(for_test=True)
    #     king=King("Black",board)
    #     possibles=king.possible_positions_diagonal_up_right(6,6)
    #     self.assertEqual(possibles,[(5,7)])

    # def test_possible_positions_diagonal_up_left(self):
    #     board=Board(for_test=True)
    #     king=King("White",board)
    #     possibles=king.possible_positions_diagonal_up_left(6,6)
    #     self.assertEqual(possibles,[(5,5)])


      