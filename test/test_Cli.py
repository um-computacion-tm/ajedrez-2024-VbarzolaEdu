import unittest
from unittest.mock import patch
from juego.chess import Chess
from juego.Cli import play
from juego.exceptions import *

class TestCli(unittest.TestCase):
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')

    #cuando vayamos a poner los mocks de los patchs, llamarlos en orden inverso. Primero al ulitmo, segundo al penultimo
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 2)  
        self.assertEqual(mock_chess_move.call_count, 1)
####################################
    #Test para cuando falla el primer input
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['hola', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)
####################################

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)
################################
    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '1'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(
        Chess,
        'move',
        side_effect=InvalidMove(),
    )

    def test_invalid_move(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)
######
    @patch("builtins.input", side_effect=["8","8","3","4"],)
    @patch("builtins.print")
    @patch.object(Chess,"move",side_effect=OriginInvalidMove())

    def test_invalid_origin_move(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)
##################################
    @patch("builtins.print")
    @patch("builtins.input",side_effect=["1","2","hola","2"])
    @patch.object(Chess,"move",side_effect=DestinationInvalidMove())

    def test_invalid_destination_move(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,3)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,0)
        