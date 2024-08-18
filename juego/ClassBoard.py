from juego.ClassRook import Rook
from juego.ClassHorse import Horse 
from juego.ClassBishop import Bishop
from juego.ClassQueen import Queen
from juego.ClassKing import King 
from juego.ClassPawn import Pawn
from juego.ClassPiece import Piece #importar la clase Rook y pieces de ClassChess.py

class Board():
    def __init__(self):
        #los indices son E8 por ejemplo. Va de 1-8 y a-h
        self.__positions__= []
        #LLenado de matriz. Primero se crean 8 filas y luego 8 columnas
        for _ in range(8):
            col=[]
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0]= Rook("Black") #black
        self.__positions__[7][7]= Rook("White") #white
        self.__positions__[0][7]= Rook("Black") #black
        self.__positions__[7][0]= Rook("White") #White
        self.__positions__[0][1]= Horse("Black")
        self.__positions__[0][6]= Horse("Black")
        self.__positions__[7][1]= Horse("White")
        self.__positions__[7][6]= Horse("White")
        self.__positions__[0][2]= Bishop("Black")
        self.__positions__[0][5]= Bishop("Black")
        self.__positions__[7][2]= Bishop("White")
        self.__positions__[7][5]= Bishop("White")
        self.__positions__[0][3]= Queen("Black")
        self.__positions__[7][3]= Queen("White")
        self.__positions__[0][4]= King("Black")
        self.__positions__[7][4]= King("White")
        #Llenado de pawns
        for i in range(8):
            self.__positions__[1][i]= Pawn("Black")
            self.__positions__[6][i]= Pawn("White")
        #metodo para obtener la posicion
        
    def get_piece(self,row,col):
        return self.__positions__[row][col]
    
