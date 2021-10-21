class Pawn:
    def __init__(self, image, color, position, name):
        self.image = image
        self.name = name
        self.position = position
        self.color = color
        self.black_start_flags = []
        self.white_start_flags = []

        if color == 'black':
            for i in range(8):
                self.black_start_flags.append(True)
            self.y = 90
            if position == '1':
                self.x = 10
            if position == '2':
                self.x = 90
            if position == '3':
                self.x = 170
            if position == '4':
                self.x = 250
            if position == '5':
                self.x = 330
            if position == '6':
                self.x = 410
            if position == '7':
                self.x = 490
            if position == '8':
                self.x = 570

        if color == 'white':
            for i in range(8):
                self.white_start_flags.append(True)
            self.y = 490
            if position == '1':
                self.x = 10
            if position == '2':
                self.x = 90
            if position == '3':
                self.x = 170
            if position == '4':
                self.x = 250
            if position == '5':
                self.x = 330
            if position == '6':
                self.x = 410
            if position == '7':
                self.x = 490
            if position == '8':
                self.x = 570

    def check_obstacles(self, x, y, color, obstacles_list, square_size, capture_flag):
        square_travel = []
        y_factor = int(abs(y - self.y)/ square_size)
        print(y_factor)
        
        for i in range(y_factor):
            if color == 'black':
                square_travel.append((self.x, self.y + (i+1) * square_size))
            else:
                square_travel.append((self.x, self.y - (i+1) * square_size))
        print(square_travel)

        for i in range(len(square_travel)):
            for j in range(len(obstacles_list)):
                    if obstacles_list[j] == square_travel[i] and not capture_flag:
                        print("Obstacle detected")
                        return True

        return False

    # If opponent piece if directly in front, pawn is blocked
    def check_capture_condition(self, x, y, color, position, square_size, capture_flag):
        if capture_flag:
            if color == 'black':
                if x == self.x + square_size and y == self.y + square_size:
                    return True
                if x == self.x - square_size and y == self.y + square_size:
                    return True

            if color == 'white':
                if x == self.x + square_size and y == self.y - square_size:
                    return True
                if x == self.x - square_size and y == self.y - square_size:
                    return True

        else:
            return False
            
    def check_constraints(self, x, y, color, position, obstacle_list, square_size, capture_flag):
        obstacle_flag = False
        position = int(position)
        passed_constraint = False
        x_constraint = abs(x - self.x)

        print (x_constraint) 
        if x_constraint == 0 or capture_flag:
            if color == 'black':
                # Legal move
                if self.black_start_flags[position - 1]:
                    if y <= self.y + (2 * square_size):
                        self.black_start_flags[position - 1] = False
                        #self.x, self.y = x, y
                        passed_constraint = True
                    else:
                        print("Invalid move")
                
                else:
                    if y == self.y + square_size:
                        #self.x, self.y = x, y
                        passed_constraint = True

                    else:
                        print("Invalid move")

            if color == 'white':
                if self.white_start_flags[position - 1]:
                    if y >= self.y - (2 * square_size):
                        self.white_start_flags[position - 1] = False
                        #self.x, self.y = x, y
                        passed_constraint = True

                    else:
                        print("Invalid move")

                else:
                    if y == self.y - square_size:
                        #self.x, self.y = x, y
                        passed_constraint = True

                    else:
                        print("Invalid move")
        else:
            return

        if passed_constraint:
            obstacle_flag = self.check_obstacles(x, y, color, obstacle_list, square_size, capture_flag)
            
            if not obstacle_flag:
                self.x, self.y = x, y
