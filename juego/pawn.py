from juego.piece import Piece

class Pawn(Piece):
    
    White_str="♟"
    Black_str= "♙"
    
    

    def valid_positions_pawn(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el peón.

        Args:
            from_row (int): La fila de origen del peón.
            from_col (int): La columna de origen del peón.
            to_row (int): La fila de destino del peón.
            to_col (int): La columna de destino del peón.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        if self.get_color() == "White":
            possibles= self.possible_positions_vertical_up(from_row, from_col) + self.first_move_vertical_up(from_row, from_col) + self.possible_capture_positions_up_right(from_row, from_col) + self.possible_capture_positions_up_left(from_row, from_col)
        if self.get_color() == "Black":
            possibles= self.possible_positions_vertical_down(from_row, from_col) + self.first_move_vertical_down(from_row, from_col) + self.possible_capture_positions_down_right(from_row, from_col) + self.possible_capture_positions_down_left(from_row, from_col)
        if possibles is not None: 
            possibles = sorted(set(possibles))
        return (to_row, to_col) in possibles

    def first_move_vertical_down(self, row, col):
        """
        Calcula las posiciones posibles para el primer movimiento vertical hacia abajo del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el primer movimiento vertical hacia abajo.
        """
        possibles = self.possible_positions_vertical_down(row, col)
        if row == 1 and len(possibles) == 1:
            other_piece = self.__board__.get_piece(row + 2, col)
            if other_piece is None:
                possibles.append((row + 2, col))
        return possibles

    def first_move_vertical_up(self, row, col):
        """
        Calcula las posiciones posibles para el primer movimiento vertical hacia arriba del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el primer movimiento vertical hacia arriba.
        """
        possibles = self.possible_positions_vertical_up(row, col)
        if row == 6 and len(possibles) == 1:
            other_piece = self.__board__.get_piece(row - 2, col)
            if other_piece is None:
                possibles.append((row - 2, col))
        return possibles
    
    def possible_positions_single_vertical(self, row, col,kr):
        """
        Calcula las posiciones posibles para los movimiento verticales en cualquier direccion del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.
            kr (int): La direccion del movimiento.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento vertical.
        """
        possibles = []
        if row + kr >= 0:
            other_piece = self.__board__.get_piece(row + kr, col)
            if other_piece is None:
                possibles.append((row + kr, col))
        return possibles
    

    def possible_positions_vertical_up(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento verticales en direccion de abajo hacia arriba del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento vertical de abajo hacia arriba del peon.
        """
        return self.possible_positions_single_vertical(row,col,-1)
    
    def possible_positions_vertical_down(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento verticales en direccion de arriba hacia abajo del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento vertical de arriba hacia abajo del peon.
        """
        return self.possible_positions_single_vertical(row,col,1)
    
    def possible_capture(self, row, col,kr,kc):
        """
        Calcula las posiciones posibles para los movimiento de captura en cualquier direccion del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.
            kr (int): La direccion del movimiento en las filas.
            kc (int): La direccion del movimiento en las columnas.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento de captura.
        """
        possibles = []
        other_piece = self.__board__.get_piece(row + kr, col + kc)
        if other_piece is not None and other_piece.get_color() != self.get_color():
            possibles.append((row + kr, col + kc))
        return possibles
            

    def possible_capture_positions_down_right(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento de captura de arriba hacia abajo, hacia la derecha, del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento de captura de arriba hacia abajo, por la derecha, del Peón.
        """
        possibles = []
        if row + 1 < 8 and col + 1 < 8:
            possibles=self.possible_capture(row,col,1,1)
        return possibles

    def possible_capture_positions_down_left(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento de captura de arriba hacia abajo, hacia la izquierda, del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento de captura de arriba hacia abajo, por la izquierda, del Peón.
        """
        possibles = []
        if row + 1 < 8 and col - 1 >= 0:
            possibles=self.possible_capture(row,col,1,-1)
        return possibles
    
    def possible_capture_positions_up_right(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento de captura de abajo hacia arriba, por la derecha, del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento de captura de abajo hacia arriba, por la derecha, del Peón.
        """
        possibles = []
        if row - 1 >= 0 and col + 1 < 8:
            possibles=self.possible_capture(row,col,-1,1)
        return possibles

    def possible_capture_positions_up_left(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento de captura de abajo hacia arriba, por la izquierda, del Peón.

        Args:
            row (int): La fila actual del peón.
            col (int): La columna actual del peón.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento de captura de abajo hacia izquierda, por la derecha, del Peón.
        """
        possibles = []
        if row - 1 >= 0 and col - 1 >= 0:
            possibles=self.possible_capture(row,col,-1,-1)
        return possibles