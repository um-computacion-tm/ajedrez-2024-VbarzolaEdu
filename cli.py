#aca tienen que estar los inpusts y prints

##pygame para darle graficos al tablero
from ClassChess import chess

def main():
    chess == chess()
    while True:
        play(chess)

def play(chess):
    
    try:
        print("turn: ", chess.turn)
        from_row= int(input("from_row"))
        from_col= int(input("from_col"))
        to_row= int(input("to_row"))
        to_col= int(input("to_col"))

    except Exception as e:
        print("Error")
        

if __name__ == "__main__":
    main()


