from juego.piece import Piece

class Knight(Piece):

    White_str = "♞"
    Black_str = "♘"
        
    def valid_positions_Knight(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el Knight.

        Args:
            from_row (int): La fila de origen del Knight.
            from_col (int): La columna de origen del Knight.
            to_row (int): La fila de destino del Knight.
            to_col (int): La columna de destino del Knight.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        possible_positions = (self.possible_positions_down(from_row, from_col) + self.possible_positions_up(from_row, from_col))
        return (to_row, to_col) in possible_positions

    def possible_positions(self, row, col, kr, kc):
        """
        Calcula las posiciones posibles para los movimiento en cualquier direccion del caballo.

        Args:
            row (int): La fila actual del caballo.
            col (int): La columna actual del caballo.
            kr (int): La direccion del movimiento.
            kc (int): La direccion del movimiento.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento del caballo.
        """
        possibles = []
        if 0 <= row + kr < 8 and 0 <= col + kc < 8:
            other_piece = self.__board__.get_piece(row + kr, col + kc)
            if other_piece is None or other_piece.__color__ != self.__color__:
                possibles.append((row + kr, col + kc))
        return possibles

    def possible_positions_down(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento en direccion de arriba hacia abajo del caballo.

        Args:
            row (int): La fila actual del caballo.
            col (int): La columna actual del caballo.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento del caballo en direccion de arriba hacia abajo.
        """
        return self.possible_positions(row, col, 2, 1) + self.possible_positions(row, col, 2, -1) + self.possible_positions(row, col, 1, 2) + self.possible_positions(row, col, 1, -2)

    def possible_positions_up(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento en direccion de abajo hacia arriba del caballo.

        Args:
            row (int): La fila actual del caballo.
            col (int): La columna actual del caballo.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento del caballo en direccion de abajo hacia arriba.
        """
        return self.possible_positions(row, col, -2, 1) + self.possible_positions(row, col, -2, -1) + self.possible_positions(row, col, -1, 2) + self.possible_positions(row, col, -1, -2)