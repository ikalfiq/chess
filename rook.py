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

    def check_obstacles(self, x, y, obstacle_list, square_size, capture_flag):
        # From current position to target position:
        # Check if there are any pieces in the way
        print(x, y)

        self.x_distance = x-self.x
        self.y_distance = y-self.y

        square_travel = []

        if self.x_distance != 0:
            for i in range(int(abs(self.x_distance)/square_size)):
                if self.x_distance > 0:
                    square_travel.append((self.x + (i+1) * square_size, self.y))
                else:
                    square_travel.append((self.x - (i+1) * square_size, self.y))
        
        else:
             for i in range(int(abs(self.y_distance)/square_size)+1):
                if self.y_distance > 0:
                    square_travel.append((self.x, self.y + (i+1) * square_size))
                else:
                    square_travel.append((self.x, self.y - (i+1) * square_size))

        print(square_travel)
        print(obstacle_list)
        
        for i in range(len(square_travel)):
            for j in range(len(obstacle_list)):
                if obstacle_list[j] == square_travel[i] and not capture_flag:
                    return True 

        return False

    def check_constraints(self, x, y, obstacle_list, square_size, capture_flag):
        if x == self.x or y == self.y:
            if self.name == 'black queen' or self.name == 'white queen':
                print('rook')
                return 'rook'
            else:
                obstacle_flag = self.check_obstacles(x, y, obstacle_list, square_size, capture_flag)

            if not obstacle_flag:
                self.x, self.y = x, y
            else:
                return
