from juego.piece import Piece

class Rook(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
      
    White_str = "♜"
    Black_str = "♖"

    def rook_move(self,from_row, from_col, to_row, to_col):
        #para mover la torre, filas deben ser iguales a las filas destino y las columnas distintas a las columnas destino. O tambien viseversa pero no ambas.
        if from_row != to_row and from_col != to_col:
            return False
        else:
            return True
    
    def valid_positions(self,from_row,from_col,to_row,to_col):
        possible_positions=(self.possible_positions_vertical_down(from_row,from_col) + self.possible_positions_vertical_up(from_row,from_col))
        
        return (to_row, to_col) in possible_positions

#metodo para verificar si la torre se puede mover desde arriba hacia abajo
    def possible_positions_vertical_down(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles    
    #metodo para verificar si la torre se puede mover desde abajo hacia arriba
    def possible_positions_vertical_up(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles
    
    #metodo para verificar si la torre se puede mover desde la derecha hacia la izquierda
    def possibles_posittiions_horizontal_right(self,row,col):
        possibles=[]
        for next_col in range(col+1,8):
            other_piece=self.__board__.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__!=self.__color__:
                    possibles.append((row,next_col))
                break
            possibles.append((row,next_col))
        return possibles
    #metodo para verificar si la torre se puede mover desde la izquierda hacia la derecha
    def possibles_positions_horizontal_left(self,row,col):
        possibles=[]
        for next_col in range(col+1,8):
            other_piece=self.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__!=self.__color__:
                    possibles.append(row,next_col)
                    break
            possibles.append((row,next_col))
        return possibles
            
    

    
    
 
