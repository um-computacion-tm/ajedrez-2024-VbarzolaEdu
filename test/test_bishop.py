from juego.bishop import Bishop
import unittest
from juego.board import Board


class TestBishop(unittest.TestCase):

    def test_diagonal_dec_rigt(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal_dec_right(0,3)
        self.assertEqual(possibles, [(1,4),(2,5),(3,6),(4,7)])
    
    def test_diagonal_dec_left(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal_dec_left(0,5)
        self.assertEqual(possibles, [(1,4),(2,3),(3,2),(4,1),(5,0)])
    
    def test_diagonal_up_left(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal_up_left(7,7)
        self.assertEqual(possibles, [(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)])
    
    def test_diagonal_up_right(self):
        board=Board(for_test=True)
        bishop= Bishop("White",board)
        possibles=bishop.possible_positions_diagonal_up_right(7,0)
        self.assertEqual(possibles, [(6,1),(5,2),(4,3),(3,4),(2,5),(1,6),(0,7)])

if __name__ == '__main__':
    unittest.main()