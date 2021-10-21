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

    
    def check_constraints(self, x, y, obstacle_list, square_size, capture_flag):
        
        posx_constraint = self.x + (2 * square_size)
        posy_constraint = self.y + (2 * square_size)
        negx_constraint = self.x - (2 * square_size)
        negy_constraint = self.y - (2 * square_size)

        if x == posx_constraint or x == negx_constraint:
            if y == self.y + square_size or y == self.y - square_size:
                self.x, self.y = x, y

        
        if y == posy_constraint or y == negy_constraint:
            if x == self.x + square_size or x == self.x - square_size:
                self.x, self.y = x, y