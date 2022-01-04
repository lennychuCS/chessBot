import numpy as np

class board():

    def __init__(self, s_fen):
        # TODO Add more of these if needed
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
        print(board_fen)

        board_index = 0
        charPointer = 0
        while board_index < 64:
            if board_index%8 == 0:
                charPointer = 0
            char = board_fen[int(board_index/8)][charPointer]
            print(new_board)
            if char.isdigit():
                print(char)
                charPointer += 1
                board_index += int(char)
            else:
                print(char)
                new_board[int(board_index/8)][board_index%8]=char
                charPointer += 1
                board_index += 1

        self.boardArray = new_board
        self.playerTurn = fen_full[1]
        self.enPassantTargets = fen_full[2]
        self.halfMoveClock = fen_full[3]
        self.fullMoveCount = fen_full[4]

    def printCurrentBoard(self):
        print(self.boardLetterToSymbol(self.boardArray))

    def boardLetterToSymbol(self, b):
        # ♔♕♖♗♘♙
        # ♚♛♜♝♞♟
        pieceMap = {
            "k":"♔",
            "q":"♕",
            "r":"♖",
            "b":"♗",
            "n":"♘",
            "p":"♙",
            "K":"♚",
            "Q":"♛",
            "R":"♜",
            "B":"♝",
            "N":"♞",
            "P":"♟",
            "":" "
        }

        nBrd = b
        for i in range(8):
            for j in range(8):
               nBrd[i,j] = pieceMap[nBrd[i,j]]

        return nBrd

