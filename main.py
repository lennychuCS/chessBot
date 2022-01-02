import numpy as np
import board
# ♔♕♖♗♘♙
# ♚♛♜♝♞♟

fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

board = board.board(fen)

board.printCurrentBoard()