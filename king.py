class King:
    def __init__(self, image, color, name):
        self.image = image
        self.name = name
        self.color = color
        self.x_distance = 0
        self.y_distance = 0

        if color == 'black':
            self.x, self.y = 330, 10
        
        if color == 'white':
            self.x , self.y = 330, 570

    def check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos):
        number_hsquares = int((abs(x-self.x))/square_size)
        number_vsquares = int((abs(y-self.y))/square_size)

        if number_hsquares == 1 or number_vsquares == 1:
            self.x, self.y = x, y
            return True
