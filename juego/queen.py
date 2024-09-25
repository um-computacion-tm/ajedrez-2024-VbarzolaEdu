from juego.piece import Piece

class Queen(Piece):
    
    White_str = "♛"
    Black_str = "♕"
        
    # def valid_positions_queen(self,from_row,from_col,to_row,to_col):
    #     return self.valid_positions_straight(from_row,from_col,to_row,to_col) + self.valid_positions_diagonal(from_row,from_col,to_row,to_col)
    
    # def valid_positions_queen(self,from_row,from_col,to_row,to_col):
    #     possible_positions=(
    #         # self.possible_positions_horizontal(from_row,from_col,1,8,1)+self.possible_positions_vertical(from_row,from_col,1,8,1)+self.possible_positions_horizontal(from_row,from_col,-1,-1,-1)+self.possible_positions_vertical(from_row,from_col,-1,-1,-1)
    #         self.move_rook(from_row,from_col)
    #         +self.move_bishop(from_row,from_col))
        
    #     return (to_row, to_col) in possible_positions

    def valid_positions_queen(self,from_row,from_col,to_row,to_col):
       return self.valid_positions_general(from_row,from_col,to_row,to_col)

        
