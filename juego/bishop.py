from juego.piece import Piece

class Bishop(Piece):
    def __str__(self):
        if self.__color__ == "White":
            return "♝"
        else:
            return "♗"
    
    def bisohp_move(self,from_row,from_col,to_row,to_col): 
        if abs(from_row - to_row) == abs(from_col - to_col):
            return True
        return False