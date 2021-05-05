import chess
import random
import player

class RandomAI(player.Player):
    def __init__(self, description = "Chess player that does random moves."):
        self.type = "AI"
        self.description = description

    def moverandom(self, board):
        legalMoves = list(board.legal_moves)
        numLegalMoves = len(legalMoves)
        if (numLegalMoves == 0):
            return -1

        randMove = random.randint(0, numLegalMoves - 1)
        return legalMoves[randMove]