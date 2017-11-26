import chess
import random
import player

class DecisionTreeAI(player.Player):
    def __init__(self, description = "Chess player that uses a decision tree.", color = chess.WHITE, depth = 3, random = False):
        self.type = "AI"
        self.description = description
        self.color = color
        self.depth = depth
        self.randomOpponent = random

    def move(self, board = chess.Board()):
        legalMoves = list(board.legal_moves)
        numLegalMoves = len(legalMoves)
        if (numLegalMoves == 0):
            return -1

        bestMoves = []
        maxScore = -2000
        for i in range(0, numLegalMoves):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            if self.randomOpponent:
                score = self.traverseExpectimaxTree(tempBoard, self.depth - 1)
            else:
                score = self.traverseMinimaxTree(tempBoard, self.depth - 1)
            if maxScore < score:
                bestMoves = []
                bestMoves.append(i)
                maxScore = score
            elif maxScore == score:
                bestMoves.append(i)

#        for i in range(0, len(bestMoves)):
#            print bestMoves[i], legalMoves[bestMoves[i]]
        randMove = random.randint(0, len(bestMoves) - 1)
        return legalMoves[bestMoves[randMove]]

    def evaluateBoard(self, board = chess.Board()):
        material =  (1 * (len(board.pieces(chess.PAWN, self.color)) - len(board.pieces(chess.PAWN, not self.color))) +
                     3 * (len(board.pieces(chess.BISHOP, self.color)) - len(board.pieces(chess.BISHOP, not self.color))) +
                     3 * (len(board.pieces(chess.KNIGHT, self.color)) - len(board.pieces(chess.KNIGHT, not self.color))) +
                     5 * (len(board.pieces(chess.ROOK, self.color)) - len(board.pieces(chess.ROOK, not self.color))) +
                     9 * (len(board.pieces(chess.QUEEN, self.color)) - len(board.pieces(chess.QUEEN, not self.color))) +
                     100 * (len(board.pieces(chess.KING, self.color)) - len(board.pieces(chess.KING, not self.color))))

        # mobility = 0.1 * len(board.legal_moves)

        return material

    def traverseMinimaxTree(self, board = chess.Board(), depth = 0):
        if depth == 0:
            return self.evaluateBoard(board)

        legalMoves = list(board.pseudo_legal_moves)
        if (len(legalMoves) == 0):
            return self.evaluateBoard(board)

        maxScore = -2000
        for i in range(0, len(legalMoves)):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            if self.randomOpponent:
                score = self.traverseExpectimaxTree(tempBoard, depth - 1)
            else:
                score = -1 * self.traverseMinimaxTree(tempBoard, depth - 1)
            if maxScore < score:
                maxScore = score
        return maxScore

    def traverseExpectimaxTree(self, board = chess.Board(), depth = 0):
        if depth == 0:
            return self.evaluateBoard(board)

        legalMoves = list(board.pseudo_legal_moves)
        if (len(legalMoves) == 0):
            return self.evaluateBoard(board)

        avgScore = 0
        for i in range(0, len(legalMoves)):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            avgScore += self.traverseMinimaxTree(tempBoard, depth - 1)
        return avgScore / len(legalMoves)