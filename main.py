import numpy as np
import board
# ♔♕♖♗♘♙
# ♚♛♜♝♞♟

fen = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"

board = board.board(fen)

board.printCurrentBoard()