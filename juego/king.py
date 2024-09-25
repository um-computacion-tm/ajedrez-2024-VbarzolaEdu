from juego.piece import Piece

class King(Piece):
   

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
    #     possible_positions = (self.possible_positions_one_move(from_row,from_col,1,1)+self.possible_positions_one_move(from_row,from_col,1,-1)+self.possible_positions_one_move(from_row,from_col,-1,1)+self.possible_positions_one_move(from_row,from_col,-1,-1)+self.possible_positions_one_move(from_row,from_col,0,1)+self.possible_positions_one_move(from_row,from_col,0,-1)+self.possible_positions_one_move(from_row,from_col,1,0)+self.possible_positions_one_move(from_row,from_col,-1,0))

    #     return (to_row, to_col) in possible_positions
    
    # def valid_positions_king(self, from_row, from_col, to_row, to_col):
    #     """
    #     Verifica si un movimiento es válido para el rey.
    
    #     Args:
    #         from_row (int): La fila de origen del rey.
    #         from_col (int): La columna de origen del rey.
    #         to_row (int): La fila de destino del rey.
    #         to_col (int): La columna de destino del rey.
    
    #     Returns:
    #         bool: True si el movimiento es válido, False en caso contrario.
    #     """
    #     # Definir todas las posibles direcciones para el rey
    #     directions = [
    #         (1, 1), (1, -1), (-1, 1), (-1, -1),  # Diagonales
    #         (0, 1), (0, -1), (1, 0), (-1, 0)     # Vertical y horizontal
    #     ]
        
    #     # Inicializar una lista para almacenar todas las posiciones posibles
    #     possible_positions = []
    
    #     # Iterar sobre las direcciones y obtener las posibles posiciones
    #     for d_row, d_col in directions:
    #         possible_positions += self.possible_positions_one_move(from_row, from_col, d_row, d_col)
    
    #     # Devolver si la posición de destino está en las posibles posiciones
    #     return (to_row, to_col) in possible_positions
    
    def valid_positions_king(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el rey.
    
        Args:
            from_row (int): La fila de origen del rey.
            from_col (int): La columna de origen del rey.
            to_row (int): La fila de destino del rey.
            to_col (int): La columna de destino del rey.
    
        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        parameters = [(1, 1), (1, -1), (-1, 1), (-1, -1),  
                        (0, 1), (0, -1), (1, 0), (-1, 0)]

        return self.valid_positions_for_one_move(from_row, from_col, to_row, to_col,parameters)
    