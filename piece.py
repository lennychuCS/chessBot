import pygame
import string
import moveIndicator as mi

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

def numToFile(a):
    foo = string.ascii_lowercase[:8]
    return foo[a]

def locToArray(x, y, size):
    col = int((x-size)/size)
    row = 7-int((y-size)/size)
    return (row, col)

def arrayToLoc(row, col, size):
    x = col*size+size
    y = (7-row)*size+size
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
        self.truePos = [numToFile(self.grid[1]),abs(self.grid[0]+1)]
        self.rect = pygame.Rect(self.pos, self.size)
        self.moveType = moves[rankColor]

    def showMoves(self, window, cb, moveIcons, turn): #cb is current board
        #Show for Cardinal Moves

        if ((turn == "w" and self.moveType[3]==0) or (turn == "b" and self.moveType[3]==1)):
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
                        center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                        if cb[gridX,gridY] == " ":
                            moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX,gridY)))
                        else:
                            if moves[cb[gridX,gridY]][3]!=self.moveType[3]:
                                moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX,gridY)))
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
                        center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                        if cb[gridX,gridY] == " ":
                            moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX,gridY)))
                        else:
                            if moves[cb[gridX,gridY]][3]!=self.moveType[3]:
                                moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX,gridY)))
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
                                center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                                if cb[gridX,gridY] == " ":
                                    moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX,gridY)))
                                else:
                                    if moves[cb[gridX,gridY]][3]!=self.moveType[3]:
                                        moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX,gridY)))

            #pawn moves
            if self.moveType[2] == 1: #White Pawns
                gridX = self.grid[0]
                gridY = self.grid[1]
                p =1
                if self.moveType[3] == 0:
                    if gridX == 1:
                        p = 2
                    for i in range(p):
                        loc = arrayToLoc(gridX+(i+1),gridY,self.size[0])
                        center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                        if gridX+i+1 < 8 and cb[gridX+(i+1),gridY] == " ":
                            moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX+(i+1),gridY)))
                        else:
                            break

                    for i in range(2): #Check for Captures
                        loc = arrayToLoc(gridX+1,gridY-1+2*i,self.size[0])
                        center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                        if gridX+1 >= 0 and gridX+1 < 8 and gridY-1+2*i >= 0 and gridY-1+2*i < 8:
                            capTarget = cb[gridX+1,gridY-1+(2*i)]
                            if capTarget != " " and moves[capTarget][3]!=self.moveType[3]:
                                moveIcons.add(mi.MoveIndicator(center,self.size[0],[gridX+1,gridY-1+(2*i)]))

                else: #Black Pawns
                    if gridX == 6:
                        p = 2
                    for i in range(p):
                        loc = arrayToLoc(gridX-(i+1),gridY,self.size[0])
                        center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                        if cb[gridX-(i+1),gridY] == " ":
                            moveIcons.add(mi.MoveIndicator(center,self.size[0],(gridX-(i+1),gridY)))
                        else:
                            break

                    for i in range(2): #Check for Captures
                        loc = arrayToLoc(gridX-1,gridY-1+(2*i),self.size[0])
                        center = ((loc[0]+self.size[0]/2)-32,(loc[1]+self.size[1]/2)-32)
                        if gridX-1 >= 0 and gridX-1 < 8 and gridY-1+(2*i) >= 0 and gridY-1+(2*i) < 8:
                            capTarget = cb[gridX-1,gridY-1+(2*i)]
                            if capTarget != " " and moves[capTarget][3]!=self.moveType[3]:
                                moveIcons.add(mi.MoveIndicator(center,self.size[0],[gridX-1,gridY-1+(2*i)]))

        moveIcons.draw(window)
        pygame.display.update()
        return moveIcons