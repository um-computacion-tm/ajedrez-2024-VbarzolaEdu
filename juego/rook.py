from juego.piece import Piece
class Rook(Piece):
    def __init__(self,color):
        super().__init__(color)
        self.__color__= color
    
      
    White_str = "♜"
    Black_str = "♖"

    def rook_move(self,from_row, from_col, to_row, to_col):
        #para mover la torre, filas deben ser iguales a las filas destino y las columnas distintas a las columnas destino. O tambien viseversa pero no ambas.
        if from_row != to_row and from_col != to_col:
            return False
        else:
            return True
        
    
 
