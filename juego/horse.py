from juego.piece import Piece

class Horse(Piece):
    def __str__(self):
        if self.__color__== "White":
            return "♞"
        else:
            return "♘"