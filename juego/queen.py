from juego.piece import Piece

class Queen(Piece):
    
    White_str = "♛"
    Black_str = "♕"
        
    def valid_positions_queen(self,from_row,from_col,to_row,to_col):
        return self.valid_positions_straight(from_row,from_col,to_row,to_col) + self.valid_positions_diagonal(from_row,from_col,to_row,to_col)
    
    
    def possible_positions_diagonal_dec(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento diagonales en direccion de arriba hacia abajo de la reina.

        Args:
            row (int): La fila actual del reina.
            col (int): La columna actual del reina.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos diagonales de arriba hacia abajo de la reina.
        """
        return self.possible_positions_diagonal(row,col,1,1)+ self.possible_positions_diagonal(row,col,1,-1) 
    
    def possible_positions_diagonal_up(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento diagonales en direccion de abajo hacia arriba la reina.

        Args:
            row (int): La fila actual del reina.
            col (int): La columna actual del reina.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos diagonales de abajo hacia arriba de la reina.
        """
        return self.possible_positions_diagonal(row,col,-1,1)+ self.possible_positions_diagonal(row,col,-1,-1)
      
    
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

        
