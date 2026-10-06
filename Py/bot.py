# ---- DEFINIMOS LA CLASE DEL BOT -------

import random 

class cpu:

    def __init__(self, size = 10):
        self.size = 10
    
    def easy_cpu(self, board):

    #Dispara aleatoriamente 
        random_shots = []
        for rows in range (self.size):
            for columns in range (self.size):
                if board [rows, columns] == '⬜' or board [rows, columns] == '⛵':
                    random_shots.append((rows, columns))

        if len(random_shots) > 0:
            return random.choice(random_shots)
        else: 
            return None

    def medium_cpu(self, board):
        hit_boxes = []
        for hit_rows in range(self.size):
            for hit_columns in range(self.size):
                if board[hit_rows, hit_columns] == '❎':
                    hit_boxes.append((hit_rows, hit_columns))

        for (hit_rows, hit_columns) in hit_boxes:
            boxes_around =[(0,1),(1,0),(-1,0),(0,-1)]
            for around_rows, around_columns in boxes_around:
                new_rows = around_rows + hit_rows
                new_columns = around_columns + hit_columns

                if new_rows >= 0 and new_rows < self.size and new_columns >= 0 and new_columns < self.size:
                    if board [new_rows, new_columns] == '⬜' or board [new_rows, new_columns] == '⛵':
                        return (new_rows, new_columns)
                    
        return self.easy_cpu(board)







            

            

                










    