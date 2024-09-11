from juego.piece import Piece

class Horse(Piece):

    White_str = "♞"
    Black_str = "♘"
        
    def horse_move(self,from_row,from_col,to_row,to_col):
        if abs(from_row - to_row)==2 and abs(from_col - to_col)==1:
            return True
        if abs(from_row - to_row)==1 and abs(from_col - to_col)==2:
            return True
        return False
    
    def valid_positions_horse(self,from_row,from_col,to_row,to_col):
        possible_positions=(self.possible_positions_down(from_row,from_col)+self.possible_positions_up(from_row,from_col)+self.possible_positions_down(from_row,from_col))
        return (to_row,to_col) in possible_positions
    
    def possible_positions(self,row,col,kr,kc):
        possibles=[]
        if 0 <= row+kr < 8 and 0 <= col+kc < 8:
            other_piece=self.__board__.get_piece(row+kr,row+kc)
            if other_piece is not None:
                if other_piece.__color__!=self.__color__:
                    possibles.append((row+kr,col+kc))
            if self.__board__.get_piece(row+kr,row+kc) is None:  
                possibles.append((row+kr,col+kc))
        return possibles
    
    def possible_positions_down(self,row,col):
        return self.possible_positions(row,col,2,3)+self.possible_positions(row,col,2,-3)+self.possible_positions(row,col,3,2)+self.possible_positions(row,col,3,-2)
    
    def possible_positions_up(self,row,col):
        return self.possible_positions(row,col,-2,3)+self.possible_positions(row,col,-2,-3)+self.possible_positions(row,col,-3,2)+self.possible_positions(row,col,-3,-2)