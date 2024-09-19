from juego.piece import Piece

class Queen(Piece):
    
    White_str = "♛"
    Black_str = "♕"
        
    def valid_positions_queen(self,from_row,from_col,to_row,to_col):
        """
        Verifica si un movimiento es válido para la reina.

        Args:
            from_row (int): La fila de origen del reina.
            from_col (int): La columna de origen del reina.
            to_row (int): La fila de destino del reina.
            to_col (int): La columna de destino del reina.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        possible_positions=(self.possible_positions_horizontal_total(from_row,from_col)+self.possible_positions_straight_total(from_row,from_col)+self.possible_positions_diagonal_dec(from_row,from_col)+self.possible_positions_diagonal_up(from_row,from_col))

        return (to_row,to_col) in possible_positions
    
    
    def possible_positions_diagonal_dec(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento diagonales en direccion de arriba hacia abajo de la reina.

        Args:
            row (int): La fila actual del reina.
            col (int): La columna actual del reina.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos diagonales de arriba hacia abajo de la reina.
        """
        return self.valid_positions_diagonal(row,col,1,1)+ self.valid_positions_diagonal(row,col,1,-1) 
    
    def possible_positions_diagonal_up(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento diagonales en direccion de abajo hacia arriba la reina.

        Args:
            row (int): La fila actual del reina.
            col (int): La columna actual del reina.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos diagonales de abajo hacia arriba de la reina.
        """
        return self.valid_positions_diagonal(row,col,-1,1)+ self.valid_positions_diagonal(row,col,-1,-1)
      
    
    def possible_positions_straight_total(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento verticales en cualquier direccion de la reina.

        Args:
            row (int): La fila actual del reina.
            col (int): La columna actual del reina.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos verticales en cualquier direccion de la reina.
        """
        return self.possible_positions_vertical(row, col, 1, 1, 8)  + self.possible_positions_vertical(row,col,-1,-1,-1)
     
    def possible_positions_horizontal_total(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento horizontales en cualquier direccion de la reina.

        Args:
            row (int): La fila actual del reina.
            col (int): La columna actual del reina.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos horizontales en cualquier direccion de la reina.
        """
        return self.possible_positions_horizontal(row,col,1,8,1) + self.possible_positions_horizontal(row,col,-1,-1,-1)

        
