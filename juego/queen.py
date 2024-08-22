from juego.piece import Piece

class Queen(Piece):
    def __str__(self):
        if self.__color__== "White":
            return "♛"
        else:
            return "♕"