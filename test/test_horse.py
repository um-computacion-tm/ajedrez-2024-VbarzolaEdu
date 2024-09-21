import unittest
from juego.knight import Knight
from juego.board import Board

class TestHorse(unittest.TestCase):
    def test_possible_positions_down(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_down(3, 3)
        expect=[(5,4), (5,2), (4, 1), (4, 5)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )
    def test_possible_positions_up(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_up(3, 3)
        expect=[(1, 2), (1, 4), (2, 1), (2, 5)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )
    def test_possible_positions(self):
        board = Board(for_test=True)
        horse = Knight("White", board)
        possibles = horse.possible_positions_up(7, 7)
        expect=[(5, 6), (6, 5)]
        self.assertEqual(
            sorted(possibles),sorted(expect)
        )