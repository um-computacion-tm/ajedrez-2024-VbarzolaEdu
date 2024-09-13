from juego.piece import Piece

class King(Piece):
    #metodo para los movimientos del rey

    White_str = "♚"
    Black_str = "♔"

    # def king_move(self,from_row,from_col,to_row,to_col):
    #     if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1:
    #         return True
    #     return False
    
    # def valid_positions_king(self,from_row,from_col,to_row,to_col):
    #     possible_positions=(self.possible_positions_vertical_down(from_row,from_col) + self.possible_positions_vertical_up(from_row,from_col)+ self.possibles_positions_horizontal_right(from_row,from_col)+self.possibles_positions_horizontal_left(from_row,from_col)+self.possible_positions_diagonal_down_right(from_row,from_col)+self.possible_positions_diagonal_down_left(from_row,from_col)+self.possible_positions_diagonal_up_right(from_row,from_col)+self.possible_positions_diagonal_up_left(from_row,from_col))
        
    #     return (to_row, to_col) in possible_positions
    
    # def possible_positions_vertical(self,row,col,kr,kc,step):
    #     possibles=[]
    #     for next_row in range(row+kr,row+kc,step):
    #         other_piece=self.__board__.get_piece(row,col)
    #         if other_piece is not None:
    #             if other_piece.__color__!=self.__color__:
    #                 possibles.append((next_row,col))
    #             break
    #         possibles.append((next_row,col))
    #     return possibles
    
    # def possible_positions_vertical_down(self,row,col):
    #     return self.possible_positions_vertical(row,col,1,2,1)
    # def possible_positions_vertical_up(self,row,col):
    #     return self.possible_positions_vertical(row,col,-1,-2,-1)
    
    # def possible_positions_horizontal(self,row,col,kr,kc,step):
    #     possibles=[]
    #     for next_col in range(col+kr,col+kc,step):
    #         other_piece=self.__board__.get_piece(row,col)
    #         if other_piece is not None:
    #             if other_piece.__color__!=self.__color__:
    #                 possibles.append((row,next_col))
    #             break
    #         possibles.append((row,next_col))
    #     return possibles
    
    # def possibles_positions_horizontal_right(self,row,col):
    #     return self.possible_positions_horizontal(row,col,1,2,1)
    # def possibles_positions_horizontal_left(self,row,col):
    #     return self.possible_positions_horizontal(row,col,-1,-2,-1)
    
    # def possible_positions_diagonal(self,row,col,kr,kc):
    #     possibles=[]
    #     other_piece=self.__board__.get_piece(row+kr,col+kc)
    #     if other_piece is not None and other_piece.__color__!=self.__color__:
    #             possibles.append((row+kr,col+kc))
    #     if other_piece is None:
    #         possibles.append((row+kr,col+kc))
    #     return possibles
    
    # def possible_positions_diagonal_down_right(self,row,col):
    #     return self.possible_positions_diagonal(row,col,1,1)
    
    # def possible_positions_diagonal_down_left(self,row,col):
    #     return self.possible_positions_diagonal(row,col,1,-1)
    
    # def possible_positions_diagonal_up_right(self,row,col):
    #     return self.possible_positions_diagonal(row,col,-1,1)
    
    # def possible_positions_diagonal_up_left(self,row,col):
    #     return self.possible_positions_diagonal(row,col,-1,-1)

    def valid_positions_king(self, from_row, from_col, to_row, to_col):
        possible_positions = (self.possible_positions_vertical_down(from_row, from_col) +
                              self.possible_positions_vertical_up(from_row, from_col) +
                              self.possible_positions_horizontal_right(from_row, from_col) +
                              self.possible_positions_horizontal_left(from_row, from_col) +
                              self.possible_positions_diagonal_all(from_row, from_col)
                           )
        return (to_row, to_col) in possible_positions

    def possible_positions_vertical_down(self, row, col):
        return self.possible_positions_vertical(row, col, 1, 2, 1)
    
    def possible_positions_diagonal_all(self,from_row,from_col):
        return  (self.possible_positions_diagonal(from_row, from_col, 1, 1) +
                self.possible_positions_diagonal(from_row, from_col, 1, -1) +
                self.possible_positions_diagonal(from_row, from_col, -1, 1) +
                self.possible_positions_diagonal(from_row, from_col, -1, -1))

    def possible_positions_vertical_up(self, row, col):
        return self.possible_positions_vertical(row, col, -1, -2, -1)

    def possible_positions_vertical(self, row, col, kr, kc, step):
        possibles = []
        for next_row in range(row + kr, row + kc, step):
            if 0 <= next_row < 8:
                other_piece = self.__board__.get_piece(next_row, col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((next_row, col))
                    break
                possibles.append((next_row, col))
        return possibles

    def possible_positions_horizontal(self, row, col, kr, kc, step):
        possibles = []
        for next_col in range(col + kr, col + kc, step):
            if 0 <= next_col < 8:
                other_piece = self.__board__.get_piece(row, next_col)
                if other_piece is not None:
                    if other_piece.__color__ != self.__color__:
                        possibles.append((row, next_col))
                    break
                possibles.append((row, next_col))
        return possibles

    def possible_positions_horizontal_right(self, row, col):
        return self.possible_positions_horizontal(row, col, 1, 2, 1)

    def possible_positions_horizontal_left(self, row, col):
        return self.possible_positions_horizontal(row, col, -1, -2, -1)

    def possible_positions_diagonal(self, row, col, kr, kc):
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