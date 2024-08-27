from juego.piece import Piece

class King(Piece):
    #metodo para los movimientos del rey
    def __str__(self):
        if self.__color__=="White":
            return "♚"
        else:
            return "♔"

    def king_move(self,from_row,from_col,to_row,to_col):
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
            return True
        return False