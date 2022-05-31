class Rook:
    def __init__(self, image, color, position, name):
        self.image = image
        self.name = name
        self.color = color
        self.x_distance = 0
        self.y_distance = 0
        
        if color == 'black':
            if position == 'left':
                self.x = 10
                self.y = 10
                
            elif position == 'right':
                self.x = 570
                self.y = 10
                
        elif color == 'white':
            if position == 'left':
                self.x = 10
                self.y = 570
                
            elif position == 'right':
                self.x = 570
                self.y = 570

    def check_king_condition(self, square_size, obstacle_list, king_pos):
        obstacle_flag = self.check_obstacles(king_pos[0], king_pos[1], obstacle_list, square_size)

        if not obstacle_flag:
            print("In check")

    def check_obstacles(self, x, y, obstacle_list, square_size):
        # From current position to target position:
        # Check if there are any pieces in the way

        self.x_distance = x-self.x
        self.y_distance = y-self.y

        square_travel = []

        if self.x_distance != 0:
            for i in range(int(abs(self.x_distance)/square_size)-1):
                if self.x_distance > 0:
                    square_travel.append((self.x + (i+1) * square_size, self.y))
                else:
                    square_travel.append((self.x - (i+1) * square_size, self.y))
        
        else:
             for i in range(int(abs(self.y_distance)/square_size)-1):
                if self.y_distance > 0:
                    square_travel.append((self.x, self.y + (i+1) * square_size))
                else:
                    square_travel.append((self.x, self.y - (i+1) * square_size))
        
        for i in range(len(square_travel)):
            for j in range(len(obstacle_list)):
                if obstacle_list[j] == square_travel[i]:
                    return True 

        return False

    def check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos):
        if x == self.x or y == self.y:
            if self.name == 'black queen' or self.name == 'white queen':
                return 'rook'
            else:
                obstacle_flag = self.check_obstacles(x, y, obstacle_list, square_size)

            if not obstacle_flag:
                self.x, self.y = x, y
                if color == 'black':
                    self.check_king_condition(square_size, obstacle_list, white_king_pos)
                else:
                    self.check_king_condition(square_size, obstacle_list, black_king_pos)
                return True
            else:
                return
