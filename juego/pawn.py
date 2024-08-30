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
    
    def valid_positions_pawn(self,from_row,from_col,to_row,to_col):
        possible_positions=(self.possible_positions_vertical_down(self,from_row,from_col)+self.possible_positions_vertical_up(self,from_row,from_col))

        return (to_row,to_col) in possible_positions
    def possible_positions_vertical_down(self,row,col):
        possibles=[]
        for next_row in range(row+1,row+2):
            other_piece=self.__board__.get_piece(row,col)
            if self.__color__!=other_piece.__color__ or self.__color__==other_piece.__color__:
                break
            possibles.append((next_row,col))

        return possibles
    
    def possible_positions_vertical_up(self,row,col):
        possibles=[]
        for next_row in range(row-1,row-2,-1):
            other_piece=self.__board__.get_piece(row,col)
            if self.__color__!=other_piece.__color__ or self.__color__==other_piece.__color__:
                break
            possibles.append((next_row,col))

        return possibles

       
#falta metodo para comerse entre piezas

