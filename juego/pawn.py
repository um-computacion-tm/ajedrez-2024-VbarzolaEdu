from juego.piece import Piece

class Pawn(Piece):
    def __str__(self):
        if self.__color__== "White":
            return "♟"
        else:
            return "♙"

