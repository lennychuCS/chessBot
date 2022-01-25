import pygame
import piece as ps

class MoveIndicator(pygame.sprite.Sprite):

    def __init__(self, loc, size, grid):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.image.load('bluecircle.png')
        self.pos = loc
        self.size = (size,size)
        self.grid = grid
        self.rect = pygame.Rect(self.pos, self.size)

    def move(self, selectedPiece, curBoard):
        oldLoc = selectedPiece.grid
        newLoc = self.grid
        curBoard.setLocValue(newLoc[0],newLoc[1], curBoard.giveLocValue(oldLoc[0],oldLoc[1]))
        curBoard.setLocValue(oldLoc[0],oldLoc[1], "")
        curBoard.printCurrentBoard()

