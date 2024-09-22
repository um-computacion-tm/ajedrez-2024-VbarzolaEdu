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
    
    
