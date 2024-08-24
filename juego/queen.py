from juego.piece import Piece

class Queen(Piece):
    def __str__(self):
        if self.__color__== "White":
            return "♛"
        else:
            return "♕"
        
    def queen_move(self,from_row,from_col,to_row,to_col):
        if from_row == to_row or from_col == to_col:
            return True
        
        #aca se replica el movimiento del alfil
        if abs(from_row - to_row) == abs(from_col - to_col):
            return True
        
        # Si no es ni en línea recta ni en diagonal, el movimiento no deberia ser valido.
        return False