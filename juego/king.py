from juego.piece import Piece

class King(Piece):
    #metodo para los movimientos del rey

    White_str = "♚"
    Black_str = "♔"


    # def valid_positions_king(self, from_row, from_col, to_row, to_col):
    #     """
    #     Verifica si un movimiento es válido para el king.

    #     Args:
    #         from_row (int): La fila de origen del king.
    #         from_col (int): La columna de origen del king.
    #         to_row (int): La fila de destino del king.
    #         to_col (int): La columna de destino del king.

    #     Returns:
    #         bool: True si el movimiento es válido, False en caso contrario.
    #     """
    #     possible_positions = (self.possible_positions_vertical_down(from_row, from_col) +
    #                           self.possible_positions_vertical_up(from_row, from_col) +
    #                           self.possible_positions_horizontal_right(from_row, from_col) +
    #                           self.possible_positions_horizontal_left(from_row, from_col) +
    #                           self.possible_positions_diagonal_all(from_row, from_col)
    #                        )
    #     return (to_row, to_col) in possible_positions

    def valid_positions_king(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el king.

        Args:
            from_row (int): La fila de origen del king.
            from_col (int): La columna de origen del king.
            to_row (int): La fila de destino del king.
            to_col (int): La columna de destino del king.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        possible_positions = (self.possible_positions_one_move(from_row,from_col,1,1)+self.possible_positions_one_move(from_row,from_col,1,-1)+self.possible_positions_one_move(from_row,from_col,-1,1)+self.possible_positions_one_move(from_row,from_col,-1,-1)+self.possible_positions_vertical(from_row,from_col,1,1,from_row + 2)+self.possible_positions_vertical(from_row,from_col,-1,-1,from_row -2)+self.possible_positions_horizontal(from_row,from_col,1,from_col+2,1)+self.possible_positions_horizontal(from_row,from_col,-1,from_col -2,-1))

        return (to_row, to_col) in possible_positions
    