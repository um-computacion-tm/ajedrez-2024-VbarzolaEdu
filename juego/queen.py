from juego.piece import Piece

class Queen(Piece):
    
    White_str = "♛"
    Black_str = "♕"
        
    def valid_positions_queen(self,from_row,from_col,to_row,to_col):
        return self.valid_positions_straight(from_row,from_col,to_row,to_col) + self.valid_positions_diagonal(from_row,from_col,to_row,to_col)
    
    

        
