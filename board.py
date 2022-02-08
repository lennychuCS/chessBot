import numpy as np


class Board():

    def __init__(self, s_fen):
        self.fen = s_fen
        self.boardArray = []
        self.fen_to_board(self.fen)
        self.playerTurn = "w"
        self.castlesLeft = "KQkq"
        self.enPassantTargets = "-"
        self.halfMoveClock = "0"
        self.fullMoveCount = "0"

    def fen_to_board(self, f):
        new_board = np.empty(shape=(8,8), dtype=str)
        fen_full = f.split(" ")
        board_fen = fen_full[0].split("/")
        #print(board_fen)

        board_index = 0
        charPointer = 0
        while board_index < 64:
            if board_index%8 == 0:
                charPointer = 0
            char = board_fen[7-int(board_index/8)][charPointer]
            #print(new_board)
            if char.isdigit():
                #print(char)
                charPointer += 1
                board_index += int(char)
            else:
                #print(char)
                new_board[int(board_index/8)][board_index%8]=char
                charPointer += 1
                board_index += 1

        self.boardArray = new_board
        self.playerTurn = fen_full[1]
        self.enPassantTargets = fen_full[2]
        self.halfMoveClock = fen_full[3]
        self.fullMoveCount = fen_full[4]

    def printCurrentBoard(self):
        b = self.boardLetterToSymbol(self.boardArray)
        spacer = "---+---+---+---+---+---+---+---"
        index = (0,0)
        for i in range (8):
            line = ""
            for j in range(8):
                line += (" " + b[i,j] + " |")
            print(line[:-1])
            if i != 7:
                print(spacer)


    def boardLetterToSymbol(self, b):
        # ♔♕♖♗♘♙
        # ♚♛♜♝♞♟
        pieceMap = {
            "K":"♔",
            "Q":"♕",
            "R":"♖",
            "B":"♗",
            "N":"♘",
            "P":"♙",
            "k":"♚",
            "q":"♛",
            "r":"♜",
            "b":"♝",
            "n":"♞",
            "p":"♟",
            "":" "
        }

        nBrd = b
        for i in range(8):
            for j in range(8):
                try:
                    nBrd[i,j] = pieceMap[nBrd[i,j]]
                except:
                    a = None
        return nBrd

    def giveLocValue(self, x, y):
        return self.boardArray[x,y]

    def setLocValue(self, x,y, newValue):
        self.boardArray[x,y] = newValue

    def nextTurn(self):
        #TODO FIX FOR PAWN MOVES/CAPTURES HALFMOVE DOESNT WORK AS IT IS "SUPPOSED" TO
        self.halfMoveClock = str(int(self.halfMoveClock) + 1)
        if self.playerTurn == "w":
            self.playerTurn = "b"
            self.fullMoveCount = str(int(self.fullMoveCount) + 1)
        else:
            self.playerTurn = "w"

    def giveHalfMove(self):
        return self.halfMoveClock

    def giveFullMove(self):
        return self.fullMoveCount

    def givePlayerTurn(self):
        return self.playerTurn