from juego.piece import Piece

class Horse(Piece):
    
    white_str = "♞"
    black_str = "♘"
        
    def horse_move(self,from_row,from_col,to_row,to_col):
        if abs(from_row - to_row)==2 and abs(from_col - to_col)==1:
            return True
        if abs(from_row - to_row)==1 and abs(from_col - to_col)==2:
            return True
        return False