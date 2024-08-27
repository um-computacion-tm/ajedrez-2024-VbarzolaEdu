class Piece:
    def __init__(self,color):
        self.__color__ = color
    
    def __str__(self):
        if self.__color__== "White":
            return self.White_str
        else:
            return self.Black_str
        