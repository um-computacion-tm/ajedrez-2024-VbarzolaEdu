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
    
    
    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        possible_positions = (
            possible_positions_vd(from_row, from_col) +
            possible_positions_va(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions#:

    def possible_positions_vd(self, row, col):
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

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles
    
 
