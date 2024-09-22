from juego.piece import Piece

class King(Piece):
    #metodo para los movimientos del rey

    White_str = "♚"
    Black_str = "♔"


    def valid_positions_king(self, from_row, from_col, to_row, to_col):
        """
        Verifica si un movimiento es válido para el king.

        Args:
            from_row (int): La fila de origen del king.
            from_col (int): La columna de origen del king.
            to_row (int): La fila de destino del king.
            to_col (int): La columna de destino del king.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """
        possible_positions = (self.possible_positions_vertical_down(from_row, from_col) +
                              self.possible_positions_vertical_up(from_row, from_col) +
                              self.possible_positions_horizontal_right(from_row, from_col) +
                              self.possible_positions_horizontal_left(from_row, from_col) +
                              self.possible_positions_diagonal_all(from_row, from_col)
                           )
        return (to_row, to_col) in possible_positions

    
    def possible_positions_vertical_down(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento verticales hacia abajo del Rey.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento vertical hacia abajo.
        """
        return self.possible_positions_vertical(row, col, 1, 1,row + 2)

    

    def possible_positions_vertical_up(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento verticales hacia arriba del Rey.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento vertical hacia arriba.
        """
        return self.possible_positions_vertical(row, col, -1, -1, row -2)

    # def possible_positions_vertical(self, row, col, kr, kc, step):
    #     """
    #     Calcula las posiciones posibles para los movimiento verticales en cualquier direccion del Rey.

    #     Args:
    #         row (int): La fila actual del rey.
    #         col (int): La columna actual del rey.
    #         kr (int): La cantidad de filas a mover.
    #         kc (int): La cantidad de columnas a mover.
    #         step (int): El paso a seguir.

    #     Returns:
    #         list: Lista de tuplas con las posiciones posibles para el rey en vertical.
    #     """
    #     possibles = []
    #     for next_row in range(row + kr, row + kc, step):
    #         if 0 <= next_row < 8:
    #             other_piece = self.__board__.get_piece(next_row, col)
    #             if other_piece is not None:
    #                 if other_piece.__color__ != self.__color__:
    #                     possibles.append((next_row, col))
    #                 break
    #             possibles.append((next_row, col))
    #     return possibles


    """
    possible_positions_vertical(self,row,col,kr,step,stop):
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
    """

    # def possible_positions_horizontal(self, row, col, kr, kc, step):
    #     """
    #     Calcula las posiciones posibles para los movimiento horizontales en cualquier direccion del Rey.

    #     Args:
    #         row (int): La fila actual del rey.
    #         col (int): La columna actual del rey.
    #         kr (int): La cantidad de filas a mover.
    #         kc (int): La cantidad de columnas a mover.
    #         step (int): El paso a seguir.

    #     Returns:
    #         list: Lista de tuplas con las posiciones posibles para el rey en horizontal.
    #     """
    #     possibles = []
    #     for next_col in range(col + kr, col + kc, step):
    #         if 0 <= next_col < 8:
    #             other_piece = self.__board__.get_piece(row, next_col)
    #             if other_piece is not None:
    #                 if other_piece.__color__ != self.__color__:
    #                     possibles.append((row, next_col))
    #                 break
    #             possibles.append((row, next_col))
    #     return possibles

    
    
    

    def possible_positions_horizontal_right(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento horizontales hacia la derecha del Rey.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento horizontales hacia la derecha.
        """
        return self.possible_positions_horizontal(row, col, 1, col+2, 1)

    def possible_positions_horizontal_left(self, row, col):
        """
        Calcula las posiciones posibles para los movimiento horizontales hacia la izquierda del Rey.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el movimiento horizontales hacia la izquierda.
        """
        return self.possible_positions_horizontal(row, col, -1, col -2, -1)

    def possible_positions_diagonal(self, row, col, kr, kc):
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
    
    def possible_positions_diagonal_all(self,from_row,from_col):
        """
        Calcula las posiciones posibles para los movimiento diagonales en cualquier direccion del Rey.

        Args:
            row (int): La fila actual del rey.
            col (int): La columna actual del rey.

        Returns:
            list: Lista de tuplas con las posiciones posibles para el rey en diagonal. Suma todas las posibles posiciones diagonales.
        """
        return  (self.possible_positions_diagonal(from_row, from_col, 1, 1) +
                self.possible_positions_diagonal(from_row, from_col, 1, -1) +
                self.possible_positions_diagonal(from_row, from_col, -1, 1) +
                self.possible_positions_diagonal(from_row, from_col, -1, -1))