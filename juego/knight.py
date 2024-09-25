from juego.piece import Piece

class Knight(Piece):

    White_str = "♞"
    Black_str = "♘"
        

    def valid_positions_knight(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el Knight.

        Args:
            from_row (int): La fila de origen del Knight.
            from_col (int): La columna de origen del Knight.
            to_row (int): La fila de destino del Knight.
            to_col (int): La columna de destino del Knight.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        parameters = [
            (2, 1), (2, -1), (1, 2), (1, -2),  # Movimientos en forma de L
            (-2, 1), (-2, -1), (-1, 2), (-1, -2)  # Movimientos en forma de L
        ]
        return  self.valid_positions_for_one_move(from_row, from_col, to_row, to_col,parameters)
        # possible_positions = (self.possible_positions_one_move(from_row, from_col,2,1)+ self.possible_positions_one_move(from_row, from_col,2,-1) + self.possible_positions_one_move(from_row, from_col,1,2) + self.possible_positions_one_move(from_row, from_col,1,-2) + self.possible_positions_one_move(from_row, from_col,-2,1) + self.possible_positions_one_move(from_row, from_col,-2,-1) + self.possible_positions_one_move(from_row, from_col,-1,2) + self.possible_positions_one_move(from_row, from_col,-1,-2))
        # return (to_row, to_col) in possible_positions

    

    