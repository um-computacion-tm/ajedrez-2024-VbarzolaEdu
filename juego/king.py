from juego.piece import Piece

class King(Piece):
    #metodo para los movimientos del rey
     def __str__(self):
        if self.__color__=="White":
            return "♚"
        else:
            return "♔"