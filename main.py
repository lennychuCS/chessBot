import numpy as np
import pygame, sys
import board
from pygame.locals import *
import piece as ps

# ♔♕♖♗♘♙
# ♚♛♜♝♞♟

fen = "rnbqkbnr/pp2pppp/8/2p5/4P3/5N2/PPP2PPP/RNBQKB1R b KQkq - 1 2"
testFen = "8/pp2pppp/8/4N3/8/PPP2PPP/8/8 b KQkq - 1 2"
square_size = 60
buffer = square = (square_size, square_size)

board = board.Board(fen)

board.printCurrentBoard()

def locToArray(x, y, size):
    col = int((x-size)/size)
    row = int((y-size)/size)
    return (row, col)

def arrayToLoc(row, col, size):
    x = col*size+size
    y = row*size+size
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
MOVESCOLOR = (162, 206, 255)

#Set up fonts
basicFont = pygame.font.SysFont(None, 48)

#Draw the white background onto the surface
windowSurface.fill(GRAY)
currentPieces = pygame.sprite.Group()

def drawBoard():

    col=0
    row=0

    while col < 8 and row < 8:

        loc = tuple(map(sum, zip((col*square_size, row*square_size), buffer)))
        if (col + row) % 2 == 0:
            pygame.draw.rect(windowSurface, WHITE, Rect(loc, square))
        else:
            pygame.draw.rect(windowSurface, SQRCOL, Rect(loc, square))

        piece = board.boardArray[row,col]
        if piece != " ":
            currentPieces.add(ps.Piece(arrayToLoc(row,col,square_size),square, piece))

        row += 1
        if row > 7:
            row = 0
            col += 1

    currentPieces.draw(windowSurface)

    #Draw the window onto the screen
    pygame.display.update()

drawBoard()

#Run the game loop
while True:

    for event in pygame.event.get():
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
          drawBoard()
          pos = pygame.mouse.get_pos()

          # get a list of all sprites that are under the mouse cursor
          clicked_sprites = [s for s in currentPieces if s.rect.collidepoint(pos)]
          for n in clicked_sprites:
            n.showMoves(windowSurface, MOVESCOLOR, board.boardArray)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

