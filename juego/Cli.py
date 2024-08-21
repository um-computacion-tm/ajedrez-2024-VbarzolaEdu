#aca tienen que estar los inpusts y prints

##pygame para darle graficos al tablero
from juego.chess import Chess

def main():
    chess = Chess()
    while Chess.is_playing():
        play(chess)


def play(chess):
    #print(chess.show_board())
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row= int(input("From row "))
        from_col= int(input("From col "))
        to_row= int(input("To row "))
        to_col= int(input("To col "))

        chess.move(from_row, from_col, to_row, to_col)

    except Exception as e:
        print("Error")

if __name__ == "__main__":
    main()


