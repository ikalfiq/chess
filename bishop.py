class Bishop:
    def __init__(self, bishop1, bishop2, coordinate1, coordinate2):
        self.bishop1=bishop1
        self.coordinate1 = coordinate1

        self.bishop2=bishop2
        self.coordinate2 = coordinate2

        print(coordinate1, coordinate2)


    def store_information(self):
         bishop = []
         bishop_coordinates = []

         bishop.append(self.bishop1)
         bishop.append(self.bishop2)

         bishop_coordinates.append(self.coordinate1)
         bishop_coordinates.append(self.coordinate2)

         print("BISHOP: ", bishop_coordinates)

