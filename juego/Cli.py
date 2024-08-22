#aca tienen que estar los inpusts y prints

##pygame para darle graficos al tablero
from juego.chess import Chess
from juego.exceptions import *

def main():
    chess = Chess()
    while Chess.is_playing():
        play(chess)


def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row= int(input("From row "))   
        from_col= int(input("From col "))
        to_row= int(input("To row "))
        to_col= int(input("To col "))

        chess.move(from_row, from_col, to_row, to_col)


#aca ponemos la llamada a las excepciones de menor a mayor jerarquia
    except OriginInvalidMove as e:
        print("El Movimiento de la fila o columna origen es invalido")
    except DestinationInvalidMove as e:
        print("El movimiento de la fila o columna destino es invalido")


    except InvalidMove as e:
        print("Invalid Move")

    except Exception as e:
        print("Error")

if __name__ == "__main__":
    main()


