import pygame

# ♔♕♖♗♘♙
# ♚♛♜♝♞♟

#in form [cardinal, diagonal, special, color], pawns are special = 1 and knights are special = 2
#white is color 0, black is color 1
moves = {
    "♔":[1,1,0,0],
    "♕":[8,8,0,0],
    "♖":[8,0,0,0],
    "♗":[0,8,0,0],
    "♘":[0,0,2,0],
    "♙":[0,0,1,0],
    "♚":[1,1,0,1],
    "♛":[8,8,0,1],
    "♜":[8,0,0,1],
    "♝":[0,8,0,1],
    "♞":[0,0,2,1],
    "♟":[0,0,1,1]
    }

def locToArray(x, y, size):
    col = int((x-size)/size)
    row = int((y-size)/size)
    return (row, col)

def arrayToLoc(row, col, size):
    x = col*size+size
    y = row*size+size
    return (x,y)

class Piece(pygame.sprite.Sprite):

    def __init__(self, pos, size, rankColor):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.rankColor = rankColor
        self.image = pygame.image.load('piecePictures/' + self.rankColor +'.png')
        self.pos = pos
        self.size = size
        self.grid = locToArray(pos[0],pos[1],self.size[0])
        self.rect = pygame.Rect(self.pos, self.size)
        self.moveType = moves[rankColor]

    def showMoves(self, window, color, cb): #cb is current board
        #Show for Cardinal Moves
        for i in range(2):
            for j in range(2):
                gridX = self.grid[0]
                gridY = self.grid[1]
                cycles = 1
                while gridX>=0 and gridX<8 and gridY>=0 and gridY<8 and cycles<=self.moveType[0]:
                    if gridX == self.grid[0] and gridY == self.grid[1]:
                        if i%2 == 0:
                            gridX += j*2-1
                        else:
                            gridY += j*2-1
                        continue
                    loc = arrayToLoc(gridX,gridY,self.size[0])
                    center = (loc[0]+self.size[0]/2,loc[1]+self.size[1]/2)
                    if cb[gridX,gridY] == " ":
                        pygame.draw.circle(window, color, center, self.size[0]/3)
                    else:
                        if moves[cb[gridX,gridY]][3]!=self.moveType[3]:
                            pygame.draw.circle(window, (200,0,0), center, self.size[0]/4)
                        break

                    if i%2 == 0:
                        gridX += j*2-1
                    else:
                        gridY += j*2-1
                    cycles+=1


        #Show for Diagonal Moves
        for i in range(2):
            for j in range(2):
                gridX = self.grid[0]
                gridY = self.grid[1]
                cycles = 1
                while gridX>=0 and gridX<8 and gridY>=0 and gridY<8 and cycles<=self.moveType[1]:
                    if gridX == self.grid[0] and gridY == self.grid[1]:
                        gridX += i*2-1
                        gridY += j*2-1
                        continue
                    loc = arrayToLoc(gridX,gridY,self.size[0])
                    center = (loc[0]+self.size[0]/2,loc[1]+self.size[1]/2)
                    if cb[gridX,gridY] == " ":
                        pygame.draw.circle(window, color, center, self.size[0]/3)
                    else:
                        if moves[cb[gridX,gridY]][3]!=self.moveType[3]:
                            pygame.draw.circle(window, (200,0,0), center, self.size[0]/4)
                        break

                    gridX += i*2-1
                    gridY += j*2-1
                    cycles+=1

        #knight moves
        lShapes = [[2,1],[1,2]]
        if self.moveType[2] == 2:
            for i in range(2):
                for j in range(2):
                    for L in lShapes:
                        gridX = self.grid[0]
                        gridY = self.grid[1]
                        gridX += L[0]*(i*2-1)
                        gridY += L[1]*(j*2-1)
                        if gridX>=0 and gridX<8 and gridY>=0 and gridY<8:
                            loc = arrayToLoc(gridX,gridY,self.size[0])
                            center = (loc[0]+self.size[0]/2,loc[1]+self.size[1]/2)
                            if cb[gridX,gridY] == " ":
                                pygame.draw.circle(window, color, center, self.size[0]/3)
                            else:
                                if moves[cb[gridX,gridY]][3]!=self.moveType[3]:
                                    pygame.draw.circle(window, (200,0,0), center, self.size[0]/4)

        #pawn moves
        if self.moveType[2] == 1:
            if self.moveType[3] == 0:
                gridX = self.grid[0]
                gridY = self.grid[1]
                if gridY == 6:
                    for i in range(2):
                        loc = arrayToLoc(gridX,gridY-(i+1),self.size[0])
                        center = (loc[0]+self.size[0]/2,loc[1]+self.size[1]/2)
                        if cb[gridX,gridY] == " ":
                            pygame.draw.circle(window, color, center, self.size[0]/3)


        pygame.display.update()

