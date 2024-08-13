from ClassPiece import piece
class Rook:
    def __init__(self, nombre, color):
        #el unico parametro de la torre que no provene de la herencia piece deberia ser un metodo que diga como se mueve
        piece.__color__ = color
        piece.__nombre__ = nombre
        pass