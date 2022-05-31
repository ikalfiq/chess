class Bishop:
    def __init__(self, image, color, position, name):
        self.image = image
        self.name = name
        self.color = color
        self.x_distance = 0
        self.y_distance = 0
        self.x_constraint_factor = 0
        self.y_constraint_factor = 0

        if color == 'black':
            if position == 'left':
                self.x = 170
                self.y = 10
                
            elif position == 'right':
                self.x = 410
                self.y = 10
                
        elif color == 'white':
            if position == 'left':
                self.x = 170
                self.y = 570
                
            elif position == 'right':
                self.x = 410
                self.y = 570

    def check_king_condition(self, square_size, obstacle_list, king_pos):
        obstacle_flag = self.check_obstacles(king_pos[0], king_pos[1], obstacle_list, square_size)

        if not obstacle_flag:
            print("In check")



    def check_obstacles(self, x, y, obstacle_list, square_size):
        square_travel = []
        self.x_distance = x - self.x
        self.y_distance = y - self.y

        if self.x_distance > 0:
            if self.y_distance > 0:
                for i in range(self.x_constraint_factor-1):
                    square_travel.append((self.x + ((i+1) * square_size), self.y + ((i+1) * square_size)))
            
            elif self.y_distance < 0:
                for i in range(self.x_constraint_factor-1):
                    square_travel.append((self.x + ((i+1) * square_size), self.y - ((i+1) * square_size)))
        
        elif self.x_distance < 0:
            if self.y_distance > 0:
                for i in range(self.x_constraint_factor-1):
                    square_travel.append((self.x - ((i+1) * square_size), self.y + ((i+1) * square_size)))
            
            elif self.y_distance < 0:
                for i in range(self.x_constraint_factor-1):
                    square_travel.append((self.x - ((i+1) * square_size), self.y - ((i+1) * square_size)))

        for i in range(len(square_travel)-1):
            for j in range(len(obstacle_list)-1):
                if obstacle_list[j] == square_travel[i]:
                    return True

        return False       


    def check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos):
        passed_constraint = False
        obstacle_flag = False

        self.x_constraint_factor = int(abs(x - self.x) / square_size)
        self.y_constraint_factor = int(abs(y - self.y) / square_size)

        if self.x_constraint_factor > 0 and self.y_constraint_factor > 0:
            if x == self.x + (self.x_constraint_factor * square_size) and y == self.y + (self.y_constraint_factor * square_size):
                passed_constraint = True

            if x == self.x - (self.x_constraint_factor * square_size) and y == self.y - (self.y_constraint_factor * square_size):
                passed_constraint = True

            if x == self.x + (self.x_constraint_factor * square_size) and y == self.y - (self.y_constraint_factor * square_size):
                passed_constraint = True

            if x == self.x - (self.x_constraint_factor * square_size) and y == self.y + (self.y_constraint_factor * square_size):
                passed_constraint = True

        
            if passed_constraint:
                if self.name == 'black queen' or self.name == 'white queen':
                    return 'bishop'
                else:
                    obstacle_flag = self.check_obstacles(x, y, obstacle_list, square_size)

            if not obstacle_flag:
                self.x, self.y = x, y
                if color == 'white':
                    self.check_king_condition(square_size, obstacle_list, black_king_pos)
                else:
                    self.check_king_condition(square_size, obstacle_list, white_king_pos)                    
                return True

