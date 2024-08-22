from juego.piece import Piece
class Rook(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.__color__= color
        
    def __str__(self):
        if self.__color__ == "White":
            return "♜"
        else:
            return "♖"

