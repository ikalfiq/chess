class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square_size = 80
        self.brown_square = (100, 50, 50)
        self.blue_square = (0, 0, 100)

        self.horizontal = []
        self.vertical = []

        for i in range(8):
            self.horizontal.append(i * self.square_size)
            self.vertical.append(i * self.square_size)

    def check_location(self, x, y):
        x_, y_ = 0, 0
        offset = 10
        for i in range(7):
            if (x > self.horizontal[i] and x < self.horizontal[i+1]):
                x_ = i * self.square_size

            if (y > self.vertical[i] and y < self.vertical[i+1]):
                y_ = i * self.square_size

            if (x > self.horizontal[7]):
                x_ = 560

            if (y > self.vertical[7]):
                y_ = 560

        return x_ + offset, y_ + offset


