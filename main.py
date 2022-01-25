import numpy as np
import pygame, sys
import board as b
from pygame.locals import *
import piece as ps

# ♔♕♖♗♘♙
# ♚♛♜♝♞♟

clock = pygame.time.Clock()
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0"
testFen = "8/pp2pppp/P1P2PPP/4N3/8/8/8/8 b KQkq - 1 2"
square_size = 60
buffer = square = (square_size, square_size)

curBoard = b.Board(fen)

curBoard.printCurrentBoard()

def locToArray(x, y, size):
    col = int((x-size)/size)
    row = 7-int((y-size)/size)
    return (row, col)

def arrayToLoc(row, col, size):
    x = col*size+size
    y = (7-row)*size+size
    return (x,y)


#Set up pygame
pygame.init()

#Set up the window
windowSurface = pygame.display.set_mode((1000, 600), 0 , 32)
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
moveIcons = pygame.sprite.Group()
selectedPiece = None

def drawBoard():

    currentPieces.empty()

    col=0
    row=0

    while col < 8 and row < 8:

        loc = tuple(map(sum, zip((row*square_size, col*square_size), buffer)))
        if (col + row) % 2 == 0:
            pygame.draw.rect(windowSurface, WHITE, Rect(loc, square))
        else:
            pygame.draw.rect(windowSurface, SQRCOL, Rect(loc, square))

        piece = curBoard.boardArray[col, row]
        if piece != " ":
            currentPieces.add(ps.Piece(arrayToLoc(col,row,square_size),square, piece))

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

    clock.tick(120)
    for event in pygame.event.get():
        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
          drawBoard()

          pos = pygame.mouse.get_pos()

          # get a list of all pieces that are under the mouse cursor
          clicked_moves = None
          clicked_moves = [s for s in moveIcons if s.rect.collidepoint(pos)]
          for n in clicked_moves:
            n.move(selectedPiece,curBoard)
            selectedPiece = None
            drawBoard()
            pos = (-1,-1)

          moveIcons.empty()

          clicked_pieces = None
          clicked_pieces = [s for s in currentPieces if s.rect.collidepoint(pos)]
          for n in clicked_pieces:
            n.showMoves(windowSurface, curBoard.boardArray, moveIcons)
            selectedPiece = n

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

