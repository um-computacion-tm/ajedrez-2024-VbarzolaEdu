from juego.board import Board
from juego.exceptions import *


class Chess():
    def __init__(self):
        self.__board__= Board()
        self.__turn__= "White"
        #metodo moverse
        #conecta con cli y usuarios, es la class que engloba o conecta board y piece
       
    def is_playing():
        return True    
    
    def move(self, from_row, from_col, to_row, to_col):
       
        if not (0 <= from_row < 8 and 0 <= from_col < 8):
         raise OriginInvalidMove()
        #validar que la posicion de origen sea valida
        if not (0<=to_row<8 and 0<=to_col<8):
            raise DestinationInvalidMove()
        #validar que la posicion de destino sea valida
        
        #validar que la pieza se pueda mover a esa posicion
        #aca iria el metodo que me permite mover la pieza
        piece = self.__board__.get_piece(from_row, from_col)

        #en algun momento, tengo que crear un metodo de piece que contenga todos los metodos para validar las piezas. Sino no logramos economizar el codigo.
        if not piece.valid_positions_rook(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        if not piece.valid_positions_pawn(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        
        #debe validar que las coordenadas sean correctas primero en un metodo distinto de move
        self.change_turn()
        

    @property
    def turn(self):
        return self.__turn__
    
    def change_turn(self):
        if self.__turn__ == "White":
            self.__turn__ = "Black"
        else:
            self.__turn__ = "White"
    
    def show_board(self):
        return str(self.__board__)
 
    def get_color(self):
        return self.__color__




