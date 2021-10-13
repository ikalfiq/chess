#!/usr/bin/env python3

class Rook:
    def __init__(self, image):
        self.image_data = image 
        self.object = []
        # Just to initialize
        self.index = (0,7)
        self.left_flag = False
        self.right_flag = False

    def set_object(self, object_r, left, right):
        #print(self.object)
        if (len(self.object) < 2):
            self.object.append(object_r)

        else:
            if (self.object[1] == self.object[0]):
                self.object.pop()

    # Arguments are indices
    def update_indices(self, flag, x, y):
        if (flag):
            self.index = (0,7)
        else:
            self.index = (x, y)

    def get_indices(self):
        return self.index

    def get_object(self):
        return self.object

    def get_image(self):
        return self.image_data

