from juego.piece import Piece

class Bishop(Piece):
    def __str__(self):
        """
        Devuelve una representación en cadena del Alfil.

        Returns:
            str: "♝" si el Alfil es blanco, "♗" si es negro.
        """
        if self.__color__ == "White":
            return "♝"
        else:
            return "♗"
    

    def valid_positions_bishop(self,from_row,from_col,to_row,to_col):
        return self.valid_positions_diagonal(from_row,from_col,to_row,to_col)
    
    
    def possible_positions_diagonal_dec_right(self,row,col):
        """
        Calcula las posiciones posibles en la diagonal decreciente hacia la derecha.

        Args:
            row (int): La fila actual del Alfil.
            col (int): La columna actual del Alfil.

        Returns:
            list: Lista de tuplas con las posiciones posibles en la diagonal decreciente hacia la derecha.
        """
        return self.possible_positions_diagonal(row,col,1,1)
    
    def possible_positions_diagonal_dec_left(self,row,col):
        """
        Calcula las posiciones posibles en la diagonal ascendente hacia la izquierda.

        Args:
            row (int): La fila actual del Alfil.
            col (int): La columna actual del Alfil.

        Returns:
            list: Lista de tuplas con las posiciones posibles en la diagonal ascendente hacia la izquierda.
        """
         
        return self.possible_positions_diagonal(row,col,1,-1)
    
    def possible_positions_diagonal_up_left(self,row,col):
        """
        Calcula las posiciones posibles en la diagonal ascendente hacia la izquierda.

        Args:
            row (int): La fila actual del Alfil.
            col (int): La columna actual del Alfil.

        Returns:
            list: Lista de tuplas con las posiciones posibles en la diagonal ascendente hacia la izquierda.
        """
        return self.possible_positions_diagonal(row,col,-1,-1)
        
    def possible_positions_diagonal_up_right(self,row,col):
        """
        Calcula las posiciones posibles en la diagonal ascendente hacia la derecha.

        Args:
            row (int): La fila actual del Alfil.
            col (int): La columna actual del Alfil.

        Returns:
            list: Lista de tuplas con las posiciones posibles en la diagonal ascendente hacia la derecha.
        """
        return self.possible_positions_diagonal(row,col,-1,1)
    
