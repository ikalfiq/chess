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

    def check_king_condition(self, square_size, obstacle_list, king_pos, piece):
        obstacle_flag = self.check_obstacles(king_pos[0], king_pos[1], obstacle_list, square_size, piece)

    def check_obstacles(self, x, y, obstacle_list, square_size, piece):
        if piece == 'rook':
            obstacle_flag = Rook.check_obstacles(self, x, y, obstacle_list, square_size)
        if piece == 'bishop':
            obstacle_flag = Bishop.check_obstacles(self, x, y, obstacle_list, square_size)

        return obstacle_flag


    def check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos):
        selected_piece = False
        if not selected_piece:
            piece = Rook.check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos)
            if piece is not None:
                selected_piece = True
        if not selected_piece:
            piece = Bishop.check_constraints(self, x, y, color, obstacle_list, square_size, black_king_pos, white_king_pos)
            if piece is not None:
                selected_piece = True

        obstacle_flag = self.check_obstacles(x, y, obstacle_list, square_size, piece)

        if not obstacle_flag:
            self.x, self.y = x, y
            if color == 'black':
                self.check_king_condition(square_size, obstacle_list, white_king_pos, piece)
            if color == 'white':
                self.check_king_condition(square_size, obstacle_list, black_king_pos, piece)
            return True
    