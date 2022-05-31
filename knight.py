from board import Board

class Knight:
    def __init__(self, image, color, position, name):
        self.image = image
        self.name = name
        self.color = color
        self.x_distance = 0
        self.y_distance = 0

        if color == 'black':
            if position == 'left':
                self.x = 90
                self.y = 10
                
            elif position == 'right':
                self.x = 490
                self.y = 10
                
        elif color == 'white':
            if position == 'left':
                self.x = 90
                self.y = 570
                
            elif position == 'right':
                self.x = 490
                self.y = 570

    def king_check_condition(self, square_size, black_king_pos, white_king_pos):
        coordinates = []
        x_list = [self.x - (2 * square_size), self.x - square_size, self.x + square_size, self.x + (2 * square_size)]
        y_list = [self.y + square_size, self.y - square_size, self.y + (2 * square_size), self.y - (2 * square_size) ]

        for i in range(4):
            for j in range(2):
                if i%2 == 0:
                    coordinates.append((x_list[i], y_list[j]))
                else:
                    coordinates.append((x_list[i], y_list[j+2]))

        for i in range(len(coordinates)):
            if coordinates[i] == black_king_pos or coordinates[i] == white_king_pos:
                print("In check")      

    def check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos):
        
        posx_constraint = self.x + (2 * square_size)
        posy_constraint = self.y + (2 * square_size)
        negx_constraint = self.x - (2 * square_size)
        negy_constraint = self.y - (2 * square_size)

        if x == posx_constraint or x == negx_constraint:
            if y == self.y + square_size or y == self.y - square_size:
                self.x, self.y = x, y
                self.king_check_condition(square_size, black_king_pos, white_king_pos)
                return True

        
        if y == posy_constraint or y == negy_constraint:
            if x == self.x + square_size or x == self.x - square_size:
                self.x, self.y = x, y
                self.king_check_condition(square_size, black_king_pos, white_king_pos)
                return True