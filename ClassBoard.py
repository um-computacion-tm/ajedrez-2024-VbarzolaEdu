from ClassChess import Rook,pieces #importar la clase Rook y pieces de ClassChess.py

class board():
    def __init__(self, nombre, color):
        #los indices son E8 por ejemplo. Va de 1-8 y a-h
        self.__positions__= []
        #LLenado de matriz. Primero se crean 8 filas y luego 8 columnas
        for i in range(8):
            col=[]
            for j in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0]= Rook("Black") #black
        self.__positions__[7][7]= Rook("White") #white
        self.__positions__[0][7]= Rook("Black") #black
        self.__positions__[7][0]= Rook("White") #White
        self.__nombre__ = nombre
        self.__color__ = color

        #metodo para obtener la posicion
        
    def get_position(self, from_row, from_col):
        return self.__positions__[from_row][from_col]