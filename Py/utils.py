
import numpy as np
import random 
from visual import slowprint

#DEFINIR FUNCIONALIDADES DEL JUEGO (Crear tableros, barcos y colocarlos)
def create_board(size = 10):
    return np.full((size, size), '⬜')

def create_ship (lenght, board):

    size = 10

    while True: #No sabemos cuantos intentos van a hacer falta 

        orientation = random.choice(['H', 'V'])

        # BARCO HORIZONTAL

        if orientation == 'H':
            row = np.random.randint(0,size) # No incluye la posicion 10 que quedaría fuera del tablero
            column = np.random.randint (0, size - lenght + 1 ) 

            '''En horizontal, limitamos la COLUMNA para que el barco no se salga por la derecha.
            Ej: Si el tablero mide 10 y el barco mide 4, el inicio máximo permitido es la columna 6 (10-4 = 6)
            NumPy excluye el último número en el rango, sumamos +1 (6 + 1 = 7) para que incluya el 6'''

        # BARCO VERTICAL

        else: 
            row = np.random.randint (0, size - lenght + 1 ) 
            column = np.random.randint(0,size)

        # CREAR BARCO

        ship = []

        for i in range (lenght): #Va añadiendo las cordenadas en las que estará el barco
            if orientation == 'H':
                ship.append((row, column + i ))
            else:
                ship.append((row + i, column))

        collision = False 
        for row, column in ship:
            if board[row, column] != '⬜':
                collision = True 
                break 
        if not collision:
             return ship


def place_ship (ship, board):
    size = 10 
    boxes_around = [(-1, -1), (-1, 1), (1, -1), (1, 1)
                    , (0,1), (1,0), (-1, 0), (0, -1)]

    for row, col in ship: #Máscara para que no esten juntos los barcos 
        for row_around, col_around in boxes_around:
            row_mask, col_mask = row_around + row, col_around + col
            if 0 <= row_mask < size and 0 <= col_mask < size:
                if board[row_mask, col_mask] == '⬜':  
                    board[row_mask, col_mask] = '⬛'

    for row, column in ship:
        board[row, column] = '⛵'
    return board 


def create_fleet (board):

    fleet_lenghts = [4,3,3,2,2,2]
    fleet_list = []

    for lenght in fleet_lenghts:
        new_ship = create_ship(lenght, board)
        board = place_ship(new_ship, board)
        fleet_list.append(new_ship)
    
    return board, fleet_list

def shoot(board, fleet_list, box=None):

    if box is None: 
        print("\n---------🔫 Es TU TURNO de disparar 🔫 -------")
        while True:
            try:
                row = int(input("Escoge una fila del 0 al 9:"))
                if 0 <= row <= 9:
                    break
                else:
                    slowprint("⚠️ ERROR ⚠️  Introducir un número del 0 al 9")
            except ValueError:
                slowprint("⚠️ ERROR ⚠️  Introducir un número del 0 al 9")

        while True:
                try:
                    column = int(input("Escoge una columna del 0 al 9:"))
                    if 0 <= column <= 9:
                        break
                    else:
                        print("⚠️ ERROR ⚠️  Introducir un número del 0 al 9")
                except:
                    if ValueError:
                        print("⚠️ ERROR ⚠️  Introducir un número del 0 al 9")

        box = (row, column )
    row, column = box 

    if board[row, column] == '⛵':
        board[row, column] = '❎'

        shipwreck = True

        for ship in fleet_list:
            if (row, column) in ship:
                for row_ship, column_ship in ship:
                    if board[row_ship, column_ship] == '⛵':
                        shipwreck = False
                        break
                if shipwreck:
                    for row_ship, column_ship in ship:
                        board[row_ship,column_ship] = '💀'
                break

        if shipwreck == False:
            slowprint(f"\nDisparo en ({row}, {column}): TOCADO 💣˖✷")
        else:
            slowprint(f"\nDisparo en ({row}, {column}): 💥 TOCADO Y HUNDIDO!!!")

    elif board[row, column] in ('⬜', '⬛'):
        board[row, column] = '💧'
        slowprint(f"\nDisparo en ({row}, {column}): AGUA ⋆｡ﾟ🌊｡")

    else:
        slowprint(f"\nYa has disparado en ({row}, {column})")

    return board

# ----VIDAS RESTANTES -------

def  lives(board):
    remaining_lives = np.sum(board == '⛵')
    return remaining_lives

# ---- MASK DEL TABLERO ENEMIGO ----

def hidden_board_cpu(board):
    hidden = board.copy()
    hidden[hidden =='⛵'] = '⬜'
    hidden[hidden == '⬛'] = '⬜'
    return hidden 

# ---- MASK DEL PLAYER ----

def hidden_board_player(board):
    hidden= board.copy()
    hidden[hidden == '⬛'] = '⬜'
    return hidden 

def lost_board_cpu(board):
    hidden= board.copy()
    hidden[hidden == '⬛'] = '⬜'
    return hidden

# --- INTERFAZ DE LA PARTIDA ----

def print_boards(player_board, cpu_board):
    import sys
    import time

    sys.stdout.write("\n📡 Escaneando tablero")
    sys.stdout.flush()
    for _ in range(3):
        time.sleep(0.3)
        sys.stdout.write(".")
        sys.stdout.flush()

    print("\n")
    time.sleep(0.2)
    cpu_hidden_board = hidden_board_cpu(cpu_board)
    player_hidden_board = hidden_board_player(player_board)

    print("\n      --- TU TABLERO ---                  --- TABLERO ENEMIGO ---")
    print("    0  1  2  3  4  5  6  7  8  9            0  1  2  3  4  5  6  7  8  9")
    print("   ---------------------------              ---------------------------")

    for r in range(10):
        player_row = " ".join(player_hidden_board[r])
        cpu_row = " ".join(cpu_hidden_board[r])
        print(f"{r} | {player_row}       {r} | {cpu_row}")

        time.sleep(0.12)


    print("\n-------------------------------------------------------------------------")

    lives_player = lives(player_board)
    lives_cpu = lives(cpu_board)

    print(f" MIS VIDAS ❤{lives_player}/16❤                                 VIDAS ENEMIGO ❤{lives_cpu}/16❤")
    print()










            








    

  