from juego.piece import Piece

class Pawn(Piece):
    
    White_str="♟"
    Black_str= "♙"
#El pawn solo puede moverse una o dos casillas hacia delante        
    def pawn_move(self,from_row,from_col,to_row,to_col):
        if self.__color__== "White":
            if from_row==to_row +1 or to_row==from_row+2:
                return True
        else:
            if from_row==to_row -1 or from_row==to_row==-2:
                return True
            
#falta metodo para comerse entre piezas

