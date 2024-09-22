from juego.piece import Piece

class Rook(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
      
    White_str = "♜"
    Black_str = "♖"

    # def rook_move(self,from_row, from_col, to_row, to_col):
    #     #para mover la torre, filas deben ser iguales a las filas destino y las columnas distintas a las columnas destino. O tambien viseversa pero no ambas.
    #     if from_row != to_row and from_col != to_col:
    #         return False
    #     else:
    #         return True
    
    def valid_positions_rook(self,from_row,from_col,to_row,to_col):
       return self.valid_positions_straight(from_row,from_col,to_row,to_col)
    
    def possible_positions_vertical_down(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento verticales en direccion de arriba hacia abajo de la torre.

        Args:
            row (int): La fila actual del torre.
            col (int): La columna actual del torre.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos verticales de arriba hacia abajo de la torre.
        """
        return self.possible_positions_vertical(row, col, 1, 1, 8) 
    
    def possible_positions_vertical_up(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento verticales en direccion de abajo hacia arriba de la torre.

        Args:
            row (int): La fila actual del torre.
            col (int): La columna actual del torre.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos verticales de abajo hacia arriba de la torre.
        """
        return self.possible_positions_vertical(row, col, -1, -1, -1)
    
    def possible_positions_horizontal_right(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento horizontales hacia la derecha de la torre.

        Args:
            row (int): La fila actual del torre.
            col (int): La columna actual del torre.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos horizontales hacia la derecha de la torre.
        """
        return self.possible_positions_horizontal(row,col,1,8,1) 
        
    def possible_positions_horizontal_left(self,row,col):
        """
        Calcula las posiciones posibles para los movimiento horizontales hacia la izquierda de la torre.

        Args:
            row (int): La fila actual del torre.
            col (int): La columna actual del torre.

        Returns:
            list: Lista de tuplas con las posiciones posibles para los movimientos horizontales hacia la izquierda de la torre.
        """
        return self.possible_positions_horizontal(row,col,-1,-1,-1)