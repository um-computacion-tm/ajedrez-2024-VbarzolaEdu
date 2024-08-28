from juego.rook import Rook
from juego.horse import Horse 
from juego.bishop import Bishop
from juego.queen import Queen
from juego.king import King 
from juego.pawn import Pawn
from juego.piece import Piece #importar la clase Rook y pieces de ClassChess.py

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


    def __str__(self):
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(f" {cell}")
                else:
                    board_str += "  "
            board_str += "\n"
        return board_str
    
        
    def get_piece(self,row,col):
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece
