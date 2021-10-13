
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
         
        self.brown_square = (100,50,50)
        self.blue_square = (0,0,100)
        self.square_size = 80
        self.horizontal = []
        self.vertical = []

        self.default_state = True

    def get_state(self):
        return self.default_state

    def set_state(self, flag):
        self.default_state = flag

    def set_zones(self, index):
        if (index < 7):
            self.horizontal.append(index*self.square_size)
            self.vertical.append(index*self.square_size)
        else:
            self.horizontal.append(index*self.square_size)
            self.vertical.append(index*self.square_size)
            self.assign_names()

    def assign_names(self):
        self.horizontal_names = {1: "A",
                                 2:"B",
                                 3:"C",
                                 4:"D",
                                 5:"E",
                                 6:"F",
                                 7:"G",
                                 8:"H"
                                 }

        self.vertical_names = {1:"1",
                                2:"2",
                                3:"3",
                                4:"4",
                                5:"5",
                                6:"6",
                                7:"7",
                                8:"8"
                                 }

    # Arguments are coordinates
    def check_zone(self, x, y):
        index = 0
        while (x > self.horizontal[index]):
            if (index < 7):
                index += 1
                horizontal_key = index
            else:
                horizontal_key = index+1
                break

        index = 0
        while (y > self.vertical[index]):
            if (index < 7):
                index += 1
                vertical_key = index
            else:
                vertical_key = index+1
                break

        print(self.horizontal_names[horizontal_key], self.vertical_names[vertical_key])
        return horizontal_key-1, vertical_key-1

    def set_blit_coordinates(self, flag, index1, index2):
        offset = 10
        if (flag):
            x_blit1, x_blit2 = self.horizontal[index1]+offset, self.horizontal[index2]+offset
            y_blit1, y_blit2 = self.vertical[index1]+offset, self.vertical[index1]+offset

            return [x_blit1, x_blit2, y_blit1, y_blit2]

        else:
            x_blit1, x_blit2 = self.horizontal[index1]+offset, self.horizontal[index2]+offset
            y_blit1, y_blit2 = self.vertical[index1]+offset, self.vertical[index2]+offset

            return [x_blit1, y_blit1, x_blit2, y_blit2]

    def get_parameters(self):
        return{"brown_square":self.brown_square, "blue_square": self.blue_square, "square_size": self.square_size} 


