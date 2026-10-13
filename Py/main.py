# La funcion vidas restantes ( cuantos Barquitos te quedan por acertar )
#Poner dificultad a la maquina. Si acierta al azar --> Tira a las adyacentes 
#Crear la funcion jugar 

from utils import create_ship, create_board, create_fleet, place_ship, shoot, lives,hidden_board_cpu, hidden_board_player, print_boards, lost_board_cpu
import numpy as np
import random
import time 
from bot import cpu  
from visual import slowprint

def play():

    slowprint("")

    slowprint("⛴️ =================Bienvenidx a Hundir la flota ====================⛴️\n")

    #Ponemos en marcha la CPU

    bot = cpu()

    dificulty = input("---------------- ⚔️ Escoge nivel de la CPU: Easy, Medium o Hard ⚔️ -----------\n").strip().lower()

    while dificulty not in ["easy","medium", "hard"]:
        slowprint("Introduce una dificultad válida")
        dificulty = input("---- ⚔️ Escoge nivel de la CPU: Easy, Medium o Hard ⚔️ ----\n").strip().lower()
    

    #Desplegamos las flotas

    slowprint("--------Prepárate, vamos a desplegar las flotas 𓇼☾𖤓ᨒ𓂃 𓈒𓏸﹏𓊝﹏----------")

    #Crear los tableros
    player_board = create_board()
    cpu_board = create_board()
    
    player_board, player_fleet = create_fleet(player_board)
    cpu_board, cpu_fleet = create_fleet(cpu_board)

    game_over = False
    turn = 1 

    while game_over == False:
        print(f"\n=======================TURNO {turn}================================")
        print_boards(player_board, cpu_board)
        slowprint("\n TU TURNO de disparar 💣")

        cpu_board = shoot(cpu_board, cpu_fleet)

        if lives(cpu_board) == 0:

            print_boards(player_board, cpu_board)
            slowprint ("\n🏆🏆🏆 ENHORABUENA!! HAS HUNDIDO LA FLOTA ENEMIGA 🏆🏆🏆")
            break
        
        
        slowprint("\n -------TURNO de la CPU-------- 🤖")

        cpu_level = {"easy": bot.easy_cpu,
                     "medium": bot.medium_cpu,
                     "hard": bot.hard_cpu}

        shot_box = cpu_level[dificulty](player_board)

        if shot_box is not None:
            player_board = shoot(player_board, player_fleet, box = shot_box)
        else:
            print("La CPU ya no tiene más casillas a las que disparar")

        if lives(player_board) == 0:

            print_boards(player_board, cpu_board)
            slowprint(f"\n☠️ ¡HAS SIDO DERROTADO en el TURNO {turn}! Todos tus barcos se han hundido ☠️")
            slowprint(f"Revelando la posición de la flota enemiga...")
            time.sleep(1.0)
            cpu_lost_board = lost_board_cpu(cpu_board)

            print("\n      --- POSICIONES DE LA CPU ---")
            print("    0  1  2  3  4  5  6  7  8  9")
            print("   ---------------------------")
            for r in range(10):
                cpu_row = " ".join(cpu_lost_board[r])
                print(f"{r} | {cpu_row}")
                time.sleep(0.12) 
            print("   Suerte la próxima vez :P\n")

            game_over = True
            break

        turn += 1 


if __name__ == "__main__":
    play()



   




    







    

    




    

    
        





        






          
