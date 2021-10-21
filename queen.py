from rook import Rook
from bishop import Bishop

class Queen:
    def __init__(self, image, color, name):
        self.image = image
        self.name = name
        self.color = color
        self.x_distance = 0
        self.y_distance = 0

        if color == 'black':
            self.x, self.y = 250, 10
        
        if color == 'white':
            self.x , self.y = 250, 570

    def check_obstacles(self, x, y, obstacle_list, square_size, capture_flag, piece):
        if piece == 'rook':
            obstacle_flag = Rook.check_obstacles(self, x, y, obstacle_list, square_size, capture_flag)
        if piece == 'bishop':
            obstacle_flag = Bishop.check_obstacles(self, x, y, obstacle_list, square_size, capture_flag)

        return obstacle_flag


    def check_constraints(self, x, y, obstacle_list, square_size, capture_flag):
        selected_piece = False
        if not selected_piece:
            print("Inside rook check")
            piece = Rook.check_constraints(self, x, y, obstacle_list, square_size, capture_flag)
            if piece is not None:
                selected_piece = True
        if not selected_piece:
            print("Inside bishop check")
            piece = Bishop.check_constraints(self, x, y, obstacle_list, square_size, capture_flag)
            if piece is not None:
                selected_piece = True

        print(selected_piece)
        print(piece)
        obstacle_flag = self.check_obstacles(x, y, obstacle_list, square_size, capture_flag, piece)

        if not obstacle_flag:
            self.x, self.y = x, y
    