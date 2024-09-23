
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
    
    def valid_move_1(self, from_row, from_col, to_row, to_col):
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
        from juego.knight import Knight
        from juego.king import King
        from juego.pawn import Pawn
        if isinstance(self, Pawn):
            return self.valid_positions_pawn(from_row, from_col, to_row, to_col)
        elif isinstance(self, Knight):
            return self.valid_positions_knight(from_row, from_col, to_row, to_col)
        elif isinstance(self, King):
            return self.valid_positions_king(from_row, from_col, to_row, to_col)
        else:
            return False
        
    def valid_move_2(self, from_row, from_col, to_row, to_col):
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
        from juego.bishop import Bishop
        from juego.queen import Queen
        if isinstance(self, Rook):
            return self.valid_positions_rook(from_row, from_col, to_row, to_col)
        elif isinstance(self, Bishop):
            return self.valid_positions_bishop(from_row, from_col, to_row, to_col)
        elif isinstance(self, Queen):
            return self.valid_positions_queen(from_row, from_col, to_row, to_col)
        else:
            return False
    

    # def valid_move(self, from_row, from_col, to_row, to_col):
    #     from juego.knight import Knight
    #     from juego.king import King
    #     from juego.pawn import Pawn
    #     from juego.rook import Rook
    #     from juego.bishop import Bishop
    #     from juego.queen import Queen
    #     """
    #     Verifica si un movimiento es válido para la pieza, dependiendo de su tipo.

    #     Args:
    #         from_row (int): La fila de origen de la pieza.
    #         from_col (int): La columna de origen de la pieza.
    #         to_row (int): La fila de destino de la pieza.
    #         to_col (int): La columna de destino de la pieza.

    #     Returns:
    #         bool: True si el movimiento es válido, False en caso contrario.
    #     """
    #     piece_validation_methods = {
    #         'Pawn': self.valid_positions_pawn,
    #         'Knight': self.valid_positions_knight,
    #         'King': self.valid_positions_king,
    #         'Rook': self.valid_positions_rook,
    #         'Bishop': self.valid_positions_bishop,
    #         'Queen': self.valid_positions_queen
    #     }

    #     # Obtenemos el tipo de la pieza
    #     piece_type = type(self).__name__

    #     # Validamos el movimiento llamando al método correspondiente
    #     if piece_type in piece_validation_methods:
    #         return piece_validation_methods[piece_type](from_row, from_col, to_row, to_col)

    #     return False






    # ##################################
    # def check_position_for_piece(self, row, col):
    #     """
    #     Verifica si hay una pieza en la posición dada y si es del color contrario.

    #     Args:
    #         row (int): La fila a verificar.
    #         col (int): La columna a verificar.

    #     Returns:
    #         tuple: Un booleano indicando si se debe detener la iteración y una lista de posibles movimientos.
    #     """
    #     possibles = []
    #     other_piece = self.__board__.get_piece(row, col)

    #     if other_piece is not None:
    #         if other_piece.__color__ != self.__color__:
    #             possibles.append((row, col))
    #         return True, possibles  # True indica que se debe detener la iteración
    #     else:
    #         possibles.append((row, col))

    #     return False, possibles  # False indica que se puede continuar



     #  metodo para n movimientos verticales.
    
    # def possible_positions_vertical(self, row, col, kr, step, stop):
    #     """
    #     Calcula las posiciones posibles para las piezas que se mueven verticalmente.

    #     Args:
    #         row (int): La fila actual de la pieza.
    #         col (int): La columna actual de la pieza.
    #         kr (int): La cantidad de filas a mover (1 o -1).
    #         step (int): El tamaño del paso de movimiento.
    #         stop (int): La fila límite para detener el movimiento.

    #     Returns:
    #         list: Lista de tuplas con las posiciones verticales posibles.
    #     """
    #     possibles = []
    #     for next_row in range(row + kr, stop, step):
    #         stop_iteration, new_possibles = self.check_position_for_piece(next_row, col)
    #         possibles.extend(new_possibles)
    #         if stop_iteration:
    #             break
    #     return possibles
    

     
    # def possible_positions_horizontal(self, row, col, kc, stop, step):
    #     """
    #     Calcula las posiciones posibles para las piezas que se mueven horizontalmente.
    
    #     Args:
    #         row (int): La fila actual de la pieza.
    #         col (int): La columna actual de la pieza.
    #         kc (int): La cantidad de columnas a mover (1 o -1).
    #         step (int): El tamaño del paso de movimiento.
    #         stop (int): La columna límite para detener el movimiento.
    
    #     Returns:
    #         list: Lista de tuplas con las posiciones horizontales posibles.
    #     """
    #     possibles = []
    #     for next_col in range(col + kc, stop, step):
    #         stop_iteration, new_possibles = self.check_position_for_piece(row, next_col)
    #         possibles.extend(new_possibles)
    #         if stop_iteration:
    #             break
    #     return possibles


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
    
    # def possible_positions_vertical(self,row,col,kr,step,stop):
    #     """
    #     Calcula las posiciones posibles para las piezas que hagan movimientos verticales.

    #     Args:
    #         row (int): La fila actual de la pieza.
    #         col (int): La columna actual del pieza.
    #         kr (int): La cantidad de filas a mover.
    #         step (int): El paso a seguir.
    #         stop (int): La fila de parada.

    #     Returns:
    #         list: Lista de tuplas con las posiciones verticales posibles.
    #     """
    #     possibles = []
    #     for next_row in range(row + kr, stop, step):
    #         possible_position = self.possible_position_check_for_piece(next_row, col)
    #         if possible_position:
    #             possibles.extend(possible_position)
    #         if self.__board__.get_piece(next_row, col) is not None:
    #             break
    #     return possibles
    

    # def possible_position_check_for_piece(self,row,col):
    #     possibles = []
    #     other_piece = self.__board__.get_piece(row, col)
    #     if other_piece is not None:
    #         if other_piece.__color__ != self.__color__:
    #             possibles.append((row, col))
    #     else:
    #         possibles.append((row, col))
    #     return possibles

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

    #metodo para n movimientos horizontales.  
    # def possible_positions_horizontal(self,row,col,kc,stop,step):
    #     """
    #     Calcula las posiciones posibles para las piezas que hagan movimientos horizontales.

    #     Args:
    #         row (int): La fila actual de la pieza.
    #         col (int): La columna actual del pieza.
    #         kc (int): La cantidad de columnas a mover.
    #         step (int): El paso a seguir.
    #         stop (int): La fila de parada.

    #     Returns:
    #         list: Lista de tuplas con las posiciones horizontales posibles.
    #     """
    #     possibles=[]
    #     for next_col in range(col+kc,stop,step):
    #         other_piece=self.__board__.get_piece(row,next_col)
    #         if other_piece is not None:
    #             if other_piece.__color__!=self.__color__:
    #                 possibles.append((row,next_col))
    #             break
    #         possibles.append((row,next_col))
    #     return possibles
    
    
    #metodo para n movimientos diagonales.
    def possible_positions_diagonal(self,row,col,kr,kc):
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
    

    #metodo para movimiento compartido unitario.

    def possible_positions_one_move(self, row, col, kr, kc):
        """
        Calcula las posiciones posibles para los movimiento diagonales en cualquier direccion del Rey.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.
            kr (int): La cantidad de filas a mover.
            kc (int): La cantidad de columnas a mover.
            step (int): El paso a seguir.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el rey en diagonal.
        """
        possibles = []
        new_row = row + kr
        new_col = col + kc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            other_piece = self.__board__.get_piece(new_row, new_col)
            if other_piece is not None and other_piece.__color__ != self.__color__:
                possibles.append((new_row, new_col))
            elif other_piece is None:
                possibles.append((new_row, new_col))
        return possibles
    
################
    ##valid positions 
    # def valid_positions_straight(self,from_row,from_col,to_row,to_col):
    #     """
    #     Verifica si un movimiento es válido para el rook.

    #     Args:
    #         from_row (int): La fila de origen del rook.
    #         from_col (int): La columna de origen del rook.
    #         to_row (int): La fila de destino del rook.
    #         to_col (int): La columna de destino del rook.

    #     Returns:
    #         bool: True si el movimiento es válido, False en caso contrario.
    #     """
    #     possible_positions=(self.possible_positions_horizontal(from_row,from_col,1,8,1)+self.possible_positions_vertical(from_row,from_col,1,1,8)+self.possible_positions_horizontal(from_row,from_col,-1,-1,-1)+self.possible_positions_vertical(from_row,from_col,-1,-1,-1))
        
    #     return (to_row, to_col) in possible_positions
    
    
    # def valid_positions_diagonal(self,from_row,from_col,to_row,to_col):
    #     """
    #     Verifica si un movimiento es válido para el rook.

    #     Args:
    #         from_row (int): La fila de origen del rook.
    #         from_col (int): La columna de origen del rook.
    #         to_row (int): La fila de destino del rook.
    #         to_col (int): La columna de destino del rook.

    #     Returns:
    #         bool: True si el movimiento es válido, False en caso contrario.
    #     """
    #     possible_positions=(self.possible_positions_diagonal(from_row,from_col,1,1)+self.possible_positions_diagonal(from_row,from_col,1,-1)+self.possible_positions_diagonal(from_row,from_col,-1,1)+self.possible_positions_diagonal(from_row,from_col,-1,-1))
    #     return (to_row, to_col) in possible_positions
        