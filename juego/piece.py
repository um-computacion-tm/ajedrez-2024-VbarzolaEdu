class Piece:
    def __init__(self,color,board):
        self.__color__ = color
        self.__board__ = board
    
    def __str__(self):
        if self.__color__== "White":
            return self.White_str
        else:
            return self.Black_str
        