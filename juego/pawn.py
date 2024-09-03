from juego.piece import Piece

class Pawn(Piece):
    
    White_str="♟"
    Black_str= "♙"
#El pawn solo puede moverse una o dos casillas hacia delante        
    # def pawn_move(self,from_row,from_col,to_row,to_col):
    #     if self.__color__== "White":
    #         if from_row==to_row +1 or to_row==from_row+2:
    #             return True
    #     else:
    #         if from_row==to_row -1 or from_row==to_row==-2:
    #             return True
    

    def valid_positions_pawn(self,from_row,from_col,to_row,to_col):
        possible_positions=(self.possible_positions_vertical_down(self,from_row,from_col)+self.possible_positions_vertical_up(self,from_row,from_col)+self.possible_capture_positions_down_right(self,from_row,from_col)+self.possible_capture_positions_down_left(self,from_row,from_col)+self.possible_capture_positions_up_right(self,from_row,from_col)+self.possible_capture_positions_up_left(self,from_row,from_col)+self.first_move_vertical_down(self,from_row,from_col)+self.first_move_vertical_up(self,from_row,from_col))
        return (to_row,to_col) in possible_positions

    #A la hota de describir todos los movimientos se aislaron por un lado los movimientos de arriba a abajo de los de abajo a arriba. Tambien se aislo los capture del peon, siendo que se uso un metodo para cuando el peon quiera comer a la diagonal izquierda y otro para cuando quiera comer a la diagonal derecha

    #consultar si es correcto que se use self al llamar los metodos en valid_positions_pawn. Y consular si es correcto se alla aislado tanto los movimientos.

    def first_move_vertical_down(self, row, col):
        possibles = self.possible_positions_vertical_down(row, col)
        #aca verifico si ya tiene casilla vacia adelante
        if row == 1 and len(possibles) == 1:
            other_piece = self.__board__.get_piece(row+2, col)
            if other_piece is None:
                possibles.append((row+2, col))
        return possibles
  

    def first_move_vertical_up(self,row,col):
        possibles=self.possible_positions_vertical_up(row,col)
        if row==6 and len(possibles)==1:
            other_piece=self.__board__.get_piece(row-2,col)
            if other_piece is None:
                possibles.append((row-2,col))

        return possibles
    
    def possible_positions_vertical_down(self,row,col):
        possibles=[]
        for next_row in range(row+1,row+2):
            other_piece=self.__board__.get_piece(row,col)
            if other_piece is not None:
                break
            possibles.append((next_row,col))
        return possibles
    
    def possible_capture_positions_down_right(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col+1)
        if other_piece is not None:
            if other_piece.__color__!=self.__color__:
                possibles.append((row+1,col+1))
        return possibles

    def possible_capture_positions_down_left(self,row,col):   
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col-1)
        if other_piece is not None:
            if other_piece.__color__!=self.__color__:
                possibles.append((row+1,col-1))
        return possibles


    def possible_positions_vertical_up(self,row,col):
        possibles=[]
        for next_row in range(row-1,row-2,-1):
            other_piece=self.__board__.get_piece(row,col)
            if other_piece is not None:
                break
            possibles.append((next_row,col))
        return possibles

    def possible_capture_positions_up_right(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col+1)
        if other_piece is not None:
            if other_piece.__color__!=self.__color__:
                possibles.append((row-1,col+1))
        return possibles
    
    def possible_capture_positions_up_left(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col-1)
        if other_piece is not None:
            if other_piece.__color__!=self.__color__:
                possibles.append((row-1,col-1))
        return possibles
    

#falta agregar test unitarios para pawn.
       
#falta metodo para comerse entre piezas

