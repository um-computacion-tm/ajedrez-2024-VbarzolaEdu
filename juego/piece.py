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