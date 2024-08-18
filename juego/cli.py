#aca tienen que estar los inpusts y prints

##pygame para darle graficos al tablero
from juego.ClassChess import Chess

def main():
    chess_instance = Chess()
    while True:
        play(chess_instance)


def play(chess_instance):
    #print(chess.show_board())
    try:
        print("turn: ", chess_instance.turn)
        from_row= int(input("From row "))
        from_col= int(input("From col "))
        to_row= int(input("To row "))
        to_col= int(input("To col "))

        chess_instance.move(from_row, from_col, to_row, to_col)

    except Exception as e:
        print("Error")
        

if __name__ == "__main__":
    main()


