from juego.piece import Piece

class King(Piece):
   

    White_str = "♚"
    Black_str = "♔"


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
        possible_positions = (self.possible_positions_one_move(from_row,from_col,1,1)+self.possible_positions_one_move(from_row,from_col,1,-1)+self.possible_positions_one_move(from_row,from_col,-1,1)+self.possible_positions_one_move(from_row,from_col,-1,-1)+self.possible_positions_one_move(from_row,from_col,0,1)+self.possible_positions_one_move(from_row,from_col,0,-1)+self.possible_positions_one_move(from_row,from_col,1,0)+self.possible_positions_one_move(from_row,from_col,-1,0))

        return (to_row, to_col) in possible_positions
    

    