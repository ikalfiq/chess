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
