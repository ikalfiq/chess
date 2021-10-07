#!/usr/bin/env python3

import pygame

pygame.init()

Display = pygame.display.set_mode((640,640))

board = pygame.Surface((10, 10))
board.fill((255,255,0))

blue = (0,0,100)
brown = (100,50,50)

size = 80 
while True:
    pygame.draw.rect(Display, brown, (0,0,640,640))
    for x in range(0, 8, 2):
        for y in range(0, 8, 1):
            pygame.draw.rect(Display, blue, ((x+(y%2))*size, y*size, size, size))

    for i in range(8):
        Display.blit(pygame.image.load('jpg_pieces/black/' + str(i+1) + '.jpg'), ((i*80+10),10))
        Display.blit(pygame.image.load('jpg_pieces/black/black_pawn.jpg'), ((i*80+10),90))
        Display.blit(pygame.image.load('jpg_pieces/white/' + str(i+1) + '.jpg'), ((i*80+10),570))
        Display.blit(pygame.image.load('jpg_pieces/white/white_pawn.jpg'), ((i*80+10),490))
    #Display.blit(pygame.image.load('jpg_pieces/black_knight.jpg'), (90,10))
    #Display.blit(pygame.image.load('jpg_pieces/black_knight.jpg'), (490,10))
    pygame.display.update()




