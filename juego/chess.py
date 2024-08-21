from juego.board import Board

class Chess():
    def __init__(self):
        self.__board__= Board()
        self.__turn__= "White"
        #metodo moverse
        #conecta con cli y usuarios, es la class que engloba o conecta board y piece
       
    def is_playing():
        return True    
    
    def move(self, from_row, from_col, to_row, to_col):
       
        #validar que la posicion de origen sea valida
        #validar que la posicion de destino sea valida
        #validar que la pieza se pueda mover a esa posicion
        #mover la pieza

        #cambio de turnos
        

        piece = self.__board__.get_piece(from_row, from_col)
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
 




