import numpy as np

class board():

    def __init__(self, s_fen):
        # TODO Add more of these if needed
        self.fen = s_fen
        self.boardArray = []
        self.fen_to_board(self.fen)
        self.playerTurn = "w"
        self.castlesLeft = "KQkq"

    def fen_to_board(self, f):
        new_board = np.empty(shape=(8,8), dtype=str)
        fen = f

        for i in range(8):
            temp = fen[:fen.find("/")]
            for j in range(8):
                try:
                    tempInt = int(temp[0])-1
                    if tempInt == 0:
                        temp = temp[1:]
                    else:
                        temp = str(tempInt) + temp[1:]
                except:
                    new_board[i,j] = temp[:1]
                    temp = temp[1:]
            if(i != 7):
                fen = fen[fen.find("/")+1:]
            else:
                fen = fen[fen.find(" ")+1:]

        self.boardArray = new_board

    def printCurrentBoard(self):
        print(self.boardLetterToSymbol(self.boardArray))

    def boardLetterToSymbol(self, b):
        nBrd = b
        # ♔♕♖♗♘♙
        # ♚♛♜♝♞♟
        for i in range(8):
            for j in range(8):
                if nBrd[i,j] == "r":
                    nBrd[i,j] = "♖"
                elif nBrd[i,j] == "n":
                     nBrd[i,j] = "♘"
                elif nBrd[i,j] == "b":
                    nBrd[i,j] = "♗"
                elif nBrd[i,j] == "q":
                    nBrd[i,j] = "♕"
                elif nBrd[i,j] == "k":
                    nBrd[i,j] = "♔"
                elif nBrd[i,j] == "p":
                    nBrd[i,j] = "♙"
                elif nBrd[i,j] == "R":
                    nBrd[i,j] = "♜"
                elif nBrd[i,j] == "N":
                    nBrd[i,j] = "♞"
                elif nBrd[i,j] == "B":
                    nBrd[i,j] = "♝"
                elif nBrd[i,j] == "Q":
                    nBrd[i,j] = "♛"
                elif nBrd[i,j] == "K":
                    nBrd[i,j] = "♚"
                elif nBrd[i,j] == "P":
                    nBrd[i,j] = "♟"
        return nBrd

