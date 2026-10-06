# La funcion vidas restantes ( cuantos Barquitos te quedan por acertar )
#Poner dificultad a la maquina. Si acierta al azar --> Tira a las adyacentes 
#Crear la funcion jugar 

from utils import create_ship, create_board, create_fleet, place_ship, shoot, lives
import numpy as np
import random
from bot import cpu  

def play():

    print("⛴️ ----Bienvenidx a Hundir la flota ----⛴️\n")

    #Crear los tableros
    player_board = create_board()
    cpu_board = create_board()

    #Crear los barcos del jugador y de la cpu

    player_board, player_fleet = create_fleet(player_board)
    cpu_board, cpu_fleet = create_fleet(cpu_board)
    #Poner en marcha la CPU

    dificulty = input("---- ⚔️ Escoge la dificultad de tu rival (Easy o Medium) ⚔️ ----\n").strip().lower()
    if dificulty == "easy":
        shot_box = cpu.easy_cpu(player_board)

    elif dificulty == "medium":
        shot_box = cpu.medium_cpu(player_board)

    else:
        print("Introduce una dificultad válida")

    if shot_box is not None:
        player_board = shoot(shot_box, player_board, player_fleet)
    else:
        print("La CPU ya no tiene más casillas a las que disparar")



    

    




    

    
        





        






          
