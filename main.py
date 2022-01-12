import numpy as np
import pygame, sys
import board
from pygame.locals import *
# ♔♕♖♗♘♙
# ♚♛♜♝♞♟

fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
testFen = "8/8/8/4b3/8/8/8/8 b KQkq - 1 2"

board = board.Board(testFen)

board.printCurrentBoard()

def locToArray(x, y):
    row = int((x-square_size)/square_size)
    col = int((y-square_size)/square_size)
    return (row, col)

def arrayToLoc(row, col):
    x = row*square_size+square_size
    y = col*square_size+square_size
    return (x,y)




#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((600, 600), 0 , 32)
pygame.display.set_caption('Chess')

#Set up the colors
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
GRAY = (100,100,100)
SQRCOL = (180,30,60)

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Draw the white background onto the surface
windowSurface.fill(GRAY)

square_size = 60
square = (square_size, square_size)

col=0
row=0
buffer = (square_size, square_size)
while col < 8 and row < 8:

    loc = tuple(map(sum, zip((col*square_size, row*square_size), buffer)))
    if (col + row) % 2 == 0:
        pygame.draw.rect(windowSurface, WHITE, Rect(loc, square))
    else:
        pygame.draw.rect(windowSurface, SQRCOL, Rect(loc, square))

    piece = board.boardArray[row,col]
    if piece != " ":
        pieceToPlace = pygame.image.load('piecePictures/' + piece + '.png')
        windowSurface.blit(pieceToPlace, loc)

    row += 1
    if row > 7:
        row = 0
        col += 1

#Draw the window onto the screen
pygame.display.update()

#Run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
