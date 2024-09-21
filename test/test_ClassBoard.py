from juego.board import Board
from juego.rook import Rook
from juego.knight import Knight
from juego.bishop import Bishop
from juego.queen import Queen
from juego.king import King
from juego.pawn import Pawn
from juego.piece import Piece
from juego.exceptions import DestinationInvalidMove, OriginInvalidMove, InvalidTurn, InvalidMove

import unittest

#test para saber si la posicion de la pieza es correcta al inicio del juego.
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=Board()
    #para las negras
    def test_get_piece(self):
        self.assertIsInstance(self.board.get_piece(0,0), Rook)
        self.assertIsInstance(self.board.get_piece(0,1), Knight)
        self.assertIsInstance(self.board.get_piece(0,2), Bishop)
        self.assertIsInstance(self.board.get_piece(0,3), Queen)
        self.assertIsInstance(self.board.get_piece(0,4), King)
        self.assertIsInstance(self.board.get_piece(0,5), Bishop)
        self.assertIsInstance(self.board.get_piece(0,6), Knight)
        self.assertIsInstance(self.board.get_piece(0,7), Rook)
       
        for i in range (8):
            piece= self.board.get_piece(1,i)
            self.assertIsInstance(piece, Pawn)
        #para blancas
        self.assertIsInstance(self.board.get_piece(7,0), Rook)
        self.assertIsInstance(self.board.get_piece(7,1), Knight)
        self.assertIsInstance(self.board.get_piece(7,2), Bishop)
        self.assertIsInstance(self.board.get_piece(7,3), Queen)
        self.assertIsInstance(self.board.get_piece(7,4), King)
        self.assertIsInstance(self.board.get_piece(7,5), Bishop)
        self.assertIsInstance(self.board.get_piece(7,6), Knight)
        self.assertIsInstance(self.board.get_piece(7,7), Rook)
        for i in range (8):
            piece= self.board.get_piece(6,i)
            self.assertIsInstance(piece, Pawn)
            #para posiciones que esten vacias en el inicio
        for i in range(2,6):
            for j in range(8):
                self.assertIsNone(self.board.get_piece(i,j))
    
#test para comprobar dimensiones de la matriz

    def test_board_dimensions(self):
        matrix = self.board.__positions__  # Asumiendo que tienes un atributo matrix
        self.assertEqual(len(matrix), 8)
        for j in matrix:
            self.assertEqual(len(j), 8)

# #test para print tablero
#     def test_str_board(self):
#         board = Board()
#         self.assertEqual(
#             str(board),
#             (   "  0 1 2 3 4 5 6 7 \n"
#                 "0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
#                 "1 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
#                 "2                 \n"
#                 "3                 \n"
#                 "4                 \n"
#                 "5                 \n"
#                 "6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
#                 "7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
#             )
#         )
    
#     def test_str_board2(self):
#         board = Board()
#         self.assertEqual(
#             str(board),
#             (   "  0 1 2 3 4 5 6 7 \n"
#                 "0 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
#                 "1 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
#                 "2                 \n"
#                 "3                 \n"
#                 "4                 \n"
#                 "5                 \n"
#                 "6 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
#                 "7 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
#             )
#         )
    #Test del move de las piezas, para saber que se mueven correctamente en el tablero
    # def test_move(self):
    #     board = Board(for_test=True)
    #     rook = Rook(color='Black', board=board)
    #     board.set_piece(0, 0, rook)

    #     board.move(
    #         from_row=0,
    #         from_col=0,
    #         to_row=0,
    #         to_col=1,
    #     )

    #     self.assertIsInstance(board.get_piece(0, 1),Rook,)
    #     self.assertEqual(
    #         str(board),
    #         (
    #             " ♖      \n"
    #             "        \n"
    #             "        \n"
    #             "        \n"
    #             "        \n"
    #             "        \n"
    #             "        \n"
    #             "        \n"
    #         )
    #     )


#este test es para ver si se levanta la excepcion que quiero
    # def test_get_piece_out_of_range(self):
    #     board = Board(for_test=True)

    #     with self.assertRaises(DestinationInvalidMove) as exc:
    #         board.get_piece(10, 10)

    #     self.assertEqual(
    #         exc.exception.message,
    #         "El movimiento de la fila o columna destino es invalido"
    #     )


if __name__ == '__main__':
    unittest.main()