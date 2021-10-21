#!/usr/bin/env python3

import pygame

from board import Board
from rook import Rook    
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from pawn import Pawn

def init_pieces():
    black_left_rook = Rook(pygame.image.load('jpg_pieces/black/rook.jpg'), 'black', 'left', "left rook")
    black_right_rook = Rook(pygame.image.load('jpg_pieces/black/rook.jpg'), 'black', 'right', "right rook")
    white_left_rook = Rook(pygame.image.load('jpg_pieces/white/rook.jpg'), 'white', 'left', "left rook")
    white_right_rook = Rook(pygame.image.load('jpg_pieces/white/rook.jpg'), 'white', 'right', "right rook")

    black_left_knight = Knight(pygame.image.load('jpg_pieces/black/knight.jpg'), 'black', 'left', 'black knight')
    black_right_knight = Knight(pygame.image.load('jpg_pieces/black/knight.jpg'), 'black', 'right', 'black knight')
    white_left_knight = Knight(pygame.image.load('jpg_pieces/white/knight.jpg'), 'white', 'left', 'white knight')
    white_right_knight = Knight(pygame.image.load('jpg_pieces/white/knight.jpg'), 'white', 'right', 'white knight')

    black_left_bishop = Bishop(pygame.image.load('jpg_pieces/black/bishop.jpg'), 'black', 'left', 'black bishop')
    black_right_bishop = Bishop(pygame.image.load('jpg_pieces/black/bishop.jpg'), 'black', 'right', 'black bishop')
    white_left_bishop = Bishop(pygame.image.load('jpg_pieces/white/bishop.jpg'), 'white', 'left', 'white bishop')
    white_right_bishop = Bishop(pygame.image.load('jpg_pieces/white/bishop.jpg'), 'white', 'right', 'white bishop')

    black_queen = Queen(pygame.image.load('jpg_pieces/black/queen.jpg'), 'black', 'black queen')
    white_queen = Queen(pygame.image.load('jpg_pieces/white/queen.jpg'), 'white' , 'white queen')

    black_king = King(pygame.image.load('jpg_pieces/black/king.jpg'), 'black', 'black king')
    white_king = King(pygame.image.load('jpg_pieces/white/king.jpg'), 'white', 'white king')

    black_pawn1 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '1', 'black pawn')
    black_pawn2 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '2', 'black pawn')
    black_pawn3 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '3', 'black pawn')
    black_pawn4 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '4', 'black pawn')
    black_pawn5 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '5', 'black pawn')
    black_pawn6 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '6', 'black pawn')
    black_pawn7 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '7', 'black pawn')
    black_pawn8 = Pawn(pygame.image.load('jpg_pieces/black/pawn.jpg'), 'black', '8', 'black pawn')

    white_pawn1 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '1', 'white pawn')
    white_pawn2 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '2', 'white pawn')
    white_pawn3 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '3', 'white pawn')
    white_pawn4 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '4', 'white pawn')
    white_pawn5 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '5', 'white pawn')
    white_pawn6 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '6', 'white pawn')
    white_pawn7 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '7', 'white pawn')
    white_pawn8 = Pawn(pygame.image.load('jpg_pieces/white/pawn.jpg'), 'white', '8', 'white pawn')

    return [black_left_rook, black_right_rook, white_left_rook, white_right_rook, black_left_knight, black_right_knight, white_left_knight, white_right_knight, black_left_bishop, black_right_bishop, white_left_bishop, white_right_bishop, black_queen, white_queen, black_king, white_king,
            black_pawn1, black_pawn2, black_pawn3, black_pawn4, black_pawn5, black_pawn6, black_pawn7, black_pawn8, 
            white_pawn1, white_pawn2, white_pawn3, white_pawn4, white_pawn5, white_pawn6, white_pawn7, white_pawn8]

if __name__== '__main__':
    pygame.init()

    width, height = 640, 640

    Display = pygame.display.set_mode((width, height))
    board_surface = pygame.Surface((10,10))
    board_surface.fill((255,255,0))

    board_layout = Board(640,640)
    square_size = board_layout.square_size

    pieces = init_pieces()
    track_id = 0

    move_flag = False
    collision_flag = False
    capture_flag = False

    while (True):            
        pygame.draw.rect(Display, board_layout.brown_square, (0, 0, width, height))

        for x in range(0, 8, 2):
            for y in range(0, 8, 1):
                blue_x = (x + (y%2)) * square_size
                blue_y = y * square_size
                pygame.draw.rect(Display, board_layout.blue_square, (blue_x, blue_y, square_size, square_size))

        objects = []
        obstacles = []

        for piece in pieces:
            obstacles.append((piece.x, piece.y))
            objects.append(Display.blit(piece.image, (piece.x, piece.y)))
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(objects)):
                        if objects[i].collidepoint(event.pos):
                            move_flag = True     
                            track_id = i    

            if move_flag:
                if event.type == pygame.MOUSEBUTTONUP:
                    for i in range(len(objects)):
                        if objects[i].collidepoint(event.pos):
                            if pieces[track_id].color == pieces[i].color: 
                                print("Collided")
                                collision_flag = True

                            else:
                                capture_flag = True
                                print("If this is a valid move, you can capture.")

                    if not collision_flag:
                        piece = pieces[track_id]
                        x, y = board_layout.check_location(event.pos[0], event.pos[1])

                        if piece.name == 'black pawn' or piece.name == 'white pawn':
                            capture_flag = piece.check_capture_condition(x, y, piece.color, piece.position, square_size, capture_flag)
                            piece.check_constraints(x, y, piece.color, piece.position, obstacles, square_size, capture_flag)
                        
                        else:
                            piece.check_constraints(x, y, obstacles, board_layout.square_size, capture_flag)
                    move_flag = False
                    collision_flag = False
                    capture_flag = False

        pygame.display.update()
