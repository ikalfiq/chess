#!/usr/bin/env python3
import pygame 

from board import Board
from rook import Rook 
from knight import Knight
from bishop import Bishop
from king import King
from queen import Queen
#from pawn import pawn

if __name__ == "__main__":

    pygame.init()

    width, height = 640, 640

    # pygame 
    Display = pygame.display.set_mode((width, height))
    board_surface = pygame.Surface((10,10))
    board_surface.fill((255,255,0))

    board_setup = Board(640,640)
    board_information = {}
    # Should extract square colors, size
    board_information = board_setup.get_parameters()
    square_size = board_information["square_size"]

    # Settle the coordinates first
    for i in range(8):
        board_setup.set_zones(i)

    # Store the piece information in a list
    black_heavy = []
    white_heavy = []

    black_pawns = []
    white_pawns = []

    rook_ = Rook(pygame.image.load('jpg_pieces/black/1.jpg'))

    while True:

        # Draw the board
        pygame.draw.rect(Display, board_information["brown_square"], (0,0,640,640))
        for x in range(0, 8, 2):
            for y in range(0, 8, 1):
                blue_x_topleft = (x+(y%2))*square_size
                blue_y_topleft = y*square_size

                pygame.draw.rect(Display, board_information["blue_square"], (blue_x_topleft, blue_y_topleft, square_size, square_size)) 

        state = board_setup.get_state()
        index1, index2 = rook_.get_indices()
        rook_.update_indices(state, index1, index2)
        coordinates = board_setup.set_blit_coordinates(state, index1, index2)
        print(coordinates)
        if (state):
            x_blit1, x_blit2, y_blit1, y_blit2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            test1, test2, test3 = 10, 570, 10
            rook_.set_object(Display.blit(rook_.get_image(), (x_blit1, y_blit1)))
            print(x_blit2)
            rook_.set_object(Display.blit(rook_.get_image(), (x_blit2, y_blit2)))
            #rook_.set_object(Display.blit(rook_.get_image(), (test1, test3)))
            #rook_.set_object(Display.blit(rook_.get_image(), (test2, test3)))

        else:
            x_blit1, y_blit1, x_blit2, y_blit2 = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
            Display.blit(rook_.get_image() ,(x_blit1, y_blit1))
            Display.blit(rook_.get_image(), (x_blit2, y_blit2))

        rook = rook_.get_object()
        #print(rook[0].center, rook[1].center)

        events = pygame.event.get()
        for event in events:
            if (event.type == pygame.MOUSEBUTTONDOWN):
                #if (rook_.get_object().collidepoint(event.pos)):
                    x,y = event.pos[0], event.pos[1]
                    index1, index2 = board_setup.check_zone(x,y)
                    print(index1, index2)
            if (event.type == pygame.MOUSEBUTTONUP):
                x,y = event.pos[0], event.pos[1]
                index1, index2 = board_setup.check_zone(x,y)
                state = False
                board_setup.set_state(state)
                rook_.update_indices(state, index1, index2)
                print(index1, index2)
       

        pygame.display.update()





