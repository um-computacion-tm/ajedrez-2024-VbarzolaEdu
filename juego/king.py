from juego.piece import Piece

class King(Piece):
    #metodo para los movimientos del rey

    white_str = "♚"
    black_str = "♔"

    def king_move(self,from_row,from_col,to_row,to_col):
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True
        return False