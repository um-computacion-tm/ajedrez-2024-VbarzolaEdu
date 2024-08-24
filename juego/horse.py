from juego.piece import Piece

class Horse(Piece):
    def __str__(self):
        if self.__color__== "White":
            return "♞"
        else:
            return "♘"
        
    def horse_move(self,from_row,from_col,to_row,to_col):
        if abs(from_row - to_row)==2 and abs(from_col - to_col)==1:
            return True
        if abs(from_row - to_row)==1 and abs(from_col - to_col)==2:
            return True
        return False