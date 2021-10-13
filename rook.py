#!/usr/bin/env python3

class Rook:
    def __init__(self, image):
        self.image_data = image 
        self.object = []
        # Just to initialize
        self.index = (0,0)

    def set_object(self, object):
        if (len(self.object) < 2):
            self.object.append(object)

        else:
            print(self.object[0].center, self.object[1].center)
            

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

