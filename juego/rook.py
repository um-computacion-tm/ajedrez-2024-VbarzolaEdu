from juego.piece import Piece

class Rook(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
      
    White_str = "♜"
    Black_str = "♖"
    
    # def valid_positions_rook(self,from_row,from_col,to_row,to_col):
    #    return self.valid_positions_straight(from_row,from_col,to_row,to_col) 

    def valid_positions_rook(self,from_row,from_col,to_row,to_col):
        possible_positions=(self.move_rook(from_row,from_col))
        
        return (to_row, to_col) in possible_positions
    
    