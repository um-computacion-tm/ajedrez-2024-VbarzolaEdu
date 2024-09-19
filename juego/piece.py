class Piece:
    def __init__(self,color,board):
        """
        Inicializa una nueva pieza de ajedrez.

        Args:
            color (str): El color de la pieza ("Black" o "White").
            board (Board): La instancia del tablero en la que se encuentra la pieza.
        """
        self.__color__ = color
        self.__board__ = board
    
    def __str__(self):
        """
        Devuelve una representación en cadena de la pieza.

        Returns:
            str: Una cadena que representa la pieza, incluyendo su color y tipo.
        """
        if self.__color__== "White":
            return self.White_str
        else:
            return self.Black_str
        
    def get_color(self):
        """
        Obtiene el color de la pieza.

        Returns:
            str: El color de la pieza ("Black" o "White").
        """
        return self.__color__
    
    def valid_move(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para la pieza.

        Este método debe ser implementado por las subclases específicas de cada tipo de pieza.

        Args:
            from_row (int): La fila de origen de la pieza.
            from_col (int): La columna de origen de la pieza.
            to_row (int): La fila de destino de la pieza.
            to_col (int): La columna de destino de la pieza.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        from juego.rook import Rook
        from juego.knight import Knight
        from juego.bishop import Bishop
        from juego.queen import Queen
        from juego.king import King
        from juego.pawn import Pawn
        if isinstance(self, Rook):
            return self.valid_positions_rook(from_row, from_col, to_row, to_col)
        elif isinstance(self, Pawn):
            return self.valid_positions_pawn(from_row, from_col, to_row, to_col)
        elif isinstance(self, Bishop):
            return self.valid_positions_bishop(from_row, from_col, to_row, to_col)
        elif isinstance(self, Knight):
            return self.valid_positions_Knight(from_row, from_col, to_row, to_col)
        elif isinstance(self, Queen):
            return self.valid_positions_queen(from_row, from_col, to_row, to_col)
        elif isinstance(self, King):
            return self.valid_positions_king(from_row, from_col, to_row, to_col)
        else:
            return False
        
    ##################################

     #metodo para n movimientos verticales.
    def possible_positions_vertical(self,row,col,kr,step,stop):
        """
        Calcula las posiciones posibles para las piezas que hagan movimientos verticales.

        Args:
            row (int): La fila actual de la pieza.
            col (int): La columna actual del pieza.
            kr (int): La cantidad de filas a mover.
            step (int): El paso a seguir.
            stop (int): La fila de parada.

        Returns:
            list: Lista de tuplas con las posiciones verticales posibles.
        """
        possibles = []
        for next_row in range(row + kr, stop, step):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles  
    
    #metodo para n movimientos horizontales.  
    def possible_positions_horizontal(self,row,col,kc,stop,step):
        """
        Calcula las posiciones posibles para las piezas que hagan movimientos horizontales.

        Args:
            row (int): La fila actual de la pieza.
            col (int): La columna actual del pieza.
            kc (int): La cantidad de columnas a mover.
            step (int): El paso a seguir.
            stop (int): La fila de parada.

        Returns:
            list: Lista de tuplas con las posiciones horizontales posibles.
        """
        possibles=[]
        for next_col in range(col+kc,stop,step):
            other_piece=self.__board__.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__!=self.__color__:
                    possibles.append((row,next_col))
                break
            possibles.append((row,next_col))
        return possibles
    
    #metodo para n movimientos diagonales.
    def valid_positions_diagonal(self,row,col,kr,kc):
        """
        Calcula las posiciones posibles para las piezas que hagan movimientos diagonales.

        Args:
            row (int): La fila actual de la pieza.
            col (int): La columna actual del pieza.
            kr (int): La cantidad de filas a mover.
            kc (int): La cantidad de columnas a mover.

        Returns:
            list: Lista de tuplas con las posiciones diagonales posibles.
        """
        possibles=[]
        next_row,next_col=row+kr,col+kc
        while 0<= next_row<8 and 8>next_col>=0:
            other_piece=self.__board__.get_piece(next_row,next_col)
            if other_piece is not None:
                    if other_piece.__color__!=self.__color__:
                        possibles.append((next_row,next_col))
                    break  
            possibles.append((next_row,next_col))
            next_row +=kr
            next_col +=kc
        return possibles
    

    