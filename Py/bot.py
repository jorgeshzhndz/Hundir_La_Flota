# ---- DEFINIMOS LA CLASE DEL BOT -------

import random 

class cpu:

    def __init__(self, size = 10):
        self.size = 10
        self.parity = random.choice([0,1])
    
    def easy_cpu(self, player_board):

    #Dispara aleatoriamente 
        random_shots = []
        for rows in range (self.size):
            for columns in range (self.size):
                if player_board [rows, columns] == '⬜' or player_board [rows, columns] == '⛵':
                    random_shots.append((rows, columns))

        if len(random_shots) > 0:
            return random.choice(random_shots)
        else: 
            return None

    def medium_cpu(self, player_board):
        hit_boxes = []
        for hit_rows in range(self.size):
            for hit_columns in range(self.size):
                if player_board[hit_rows, hit_columns] == '❎':
                    hit_boxes.append((hit_rows, hit_columns))

        for (hit_rows, hit_columns) in hit_boxes:
            boxes_around =[(0,1),(1,0),(-1,0),(0,-1)]
            for around_rows, around_columns in boxes_around:
                new_rows = around_rows + hit_rows
                new_columns = around_columns + hit_columns

                if new_rows >= 0 and new_rows < self.size and new_columns >= 0 and new_columns < self.size:
                    if player_board [new_rows, new_columns] == '⬜' or player_board [new_rows, new_columns] == '⛵':
                        return (new_rows, new_columns)
                    
        return self.easy_cpu(player_board)

    def hard_cpu(self, player_board):

        #Si hay barcos sin hundir que ha encontrado, dispara alrededor:

        hit_boxes = []
        for hit_rows in range(self.size):
            for hit_columns in range(self.size):
                if player_board[hit_rows, hit_columns] == '❎':
                    hit_boxes.append((hit_rows, hit_columns))

        if len(hit_boxes) > 0:
            return self.medium_cpu(player_board)

        # Si no hay ningún tocado aún por hundir, dispara como si fuese un tablero de ajedrez/por pares:
        #porque ningun barco mide menos de dos casillas

        pair_boxes = []
        for pair_rows in range (self.size):
            for pair_columns in range(self.size):
                pair_box = player_board[pair_rows, pair_columns] 
                if pair_box in ('⬜','⛵'):
                    
                    if (pair_rows + pair_columns)%2 == self.parity: #elige un patron (impares o pares)
                        pair_boxes.append((pair_rows, pair_columns))

        if len(pair_boxes) > 0:
            return random.choice(pair_boxes)

        # si ya no le quedan casillas pares/impares del tablero. vuelve a disparar a cualquiera 

        return self.easy_cpu(player_board)
        

        















            

            

                










    