import chess
import random
import player
import numpy as np


class DecisionTreeAI(player.Player):
    def __init__(self, description="Chess player that uses a decision tree.", color=chess.WHITE, depth=3, random=False,
                 epsilon=0, offensive=True, defensive=True):
        self.type = "AI"
        self.description = description
        self.color = color
        self.depth = depth
        self.randomOpponent = random
        self.epsilon = epsilon
        self.offensive = offensive
        self.defensive = defensive
        self.count = 0
        self.prunecount = 0
        self.count_exp = 0

    def move(self, board=chess.Board()):
        legalMoves = list(board.legal_moves)
        numLegalMoves = len(legalMoves)
        if (numLegalMoves == 0):
            return -1

        if self.epsilon > np.random.rand():
            randMove = random.randint(0, numLegalMoves - 1)
            return legalMoves[randMove]

        bestMoves = []
        maxScore = -20000
        #print(numLegalMoves)
        for i in range(0, numLegalMoves):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            if self.randomOpponent:
                score = self.traverseExpectimaxTree(tempBoard, self.depth)
            else:
                score = self.traverseMinimaxTree(tempBoard, self.depth, False)
            if maxScore < score:
                bestMoves = []
                bestMoves.append(i)
                maxScore = score
            elif maxScore == score:
                bestMoves.append(i)

        #        for i in range(0, len(bestMoves)):
        #            print bestMoves[i], legalMoves[bestMoves[i]]
        randMove = random.randint(0, len(bestMoves) - 1)
        #         print('Best Move', legalMoves[bestMoves[randMove]], 'with score', maxScore, 'out of', legalMoves)

        print('number of state evaluations = ', self.count)
        print('number of prunes = ', self.prunecount)
        return legalMoves[bestMoves[randMove]]

    def evaluateBoard(self, board=chess.Board()):
        score = (1 * (len(board.pieces(chess.PAWN, self.color)) - len(board.pieces(chess.PAWN, not self.color))) +
                    3 * (len(board.pieces(chess.BISHOP, self.color)) - len(
                    board.pieces(chess.BISHOP, not self.color))) +
                    3 * (len(board.pieces(chess.KNIGHT, self.color)) - len(
                    board.pieces(chess.KNIGHT, not self.color))) +
                    5 * (len(board.pieces(chess.ROOK, self.color)) - len(board.pieces(chess.ROOK, not self.color))) +
                    9 * (len(board.pieces(chess.QUEEN, self.color)) - len(board.pieces(chess.QUEEN, not self.color))) +
                    100 * (len(board.pieces(chess.KING, self.color)) - len(board.pieces(chess.KING, not self.color))))

        # mobility = 0.1 * len(board.legal_moves)

        return score



    def traverseMinimaxTree(self, board=chess.Board(), depth=0, isMax=True, alpha = float('-inf'), beta = float('inf')):
        legalMoves = list(board.legal_moves)
        if depth == 0 or len(legalMoves) == 0:
            score = self.evaluateBoard(board)
            self.count += 1
            if not isMax and self.offensive:
                if board.is_check():
                    score += 50
                if board.is_checkmate():
                    score += 5000
            elif self.defensive:
                if board.is_check():
                    score -= 50
                if board.is_checkmate():
                    score -= 5000
            return score

        minimaxScore = float('-inf') if isMax else float('inf')
        for i in range(0, len(legalMoves)):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            if isMax:
                #print(alpha, beta)
                if self.randomOpponent:
                    score = self.traverseExpectimaxTree(tempBoard, depth - 1)
                else:
                    score = self.traverseMinimaxTree(tempBoard, depth - 1, False, alpha=alpha, beta=beta)
                if minimaxScore < score:
                    minimaxScore = score
                alpha = max(alpha, score)
                if beta <= alpha:
                    self.prunecount += 1
                #    print('white')
                    break
            else:
                #print(alpha, beta)
                score= self.traverseMinimaxTree(tempBoard, depth - 1, True, alpha=alpha, beta=beta)
                if minimaxScore > score:
                    minimaxScore = score

                beta = min(beta, score)
                if beta <= alpha:
                    #print('black')
                    self.prunecount += 1
                    break
        return minimaxScore

    def traverseExpectimaxTree(self, board=chess.Board(), depth=0):
        legalMoves = list(board.legal_moves)
        if depth == 0 or len(legalMoves) == 0:
            score = self.evaluateBoard(board)
            self.count_exp += 1

            if self.offensive:
                if board.is_check():
                    score += 50
                if board.is_checkmate():
                    score += 5000
            return score

        avgScore = 0
        for i in range(0, len(legalMoves)):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            avgScore += self.traverseMinimaxTree(tempBoard, depth - 1)
        return avgScore / len(legalMoves)