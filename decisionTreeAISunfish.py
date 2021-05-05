import chess
import chess.engine
import random
import player
import numpy as np
import random
import pandas as pd

#For Sunfish evaluation
piece = { 'P': 100, 'N': 280, 'B': 320, 'R': 479, 'Q': 929, 'K': 60000 }
A1, H1, A8, H8 = 91, 98, 21, 28
pst = {
    'P': (    0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0),
    'N': ( -50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50),
    'B': ( -20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20),
    'R': (  0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0),
    'Q': (  -20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20),
    'K': (  -30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20),

#'P': (   0,   0,   0,   0,   0,   0,   0,   0,
    #         78,  83,  86,  73, 102,  82,  85,  90,
    #          7,  29,  21,  44,  40,  31,  44,   7,
    #        -17,  16,  -2,  15,  14,   0,  15, -13,
    #        -26,   3,  10,   9,   6,   1,   0, -23,
    #        -22,   9,   5, -11, -10,  -2,   3, -19,
    #        -31,   8,  -7, -37, -36, -14,   3, -31,
    #          0,   0,   0,   0,   0,   0,   0,   0),
    # 'N': ( -66, -53, -75, -75, -10, -55, -58, -70,
    #         -3,  -6, 100, -36,   4,  62,  -4, -14,
    #         10,  67,   1,  74,  73,  27,  62,  -2,
    #         24,  24,  45,  37,  33,  41,  25,  17,
    #         -1,   5,  31,  21,  22,  35,   2,   0,
    #        -18,  10,  13,  22,  18,  15,  11, -14,
    #        -23, -15,   2,   0,   2,   0, -23, -20,
    #        -74, -23, -26, -24, -19, -35, -22, -69),
    # 'B': ( -59, -78, -82, -76, -23,-107, -37, -50,
    #        -11,  20,  35, -42, -39,  31,   2, -22,
    #         -9,  39, -32,  41,  52, -10,  28, -14,
    #         25,  17,  20,  34,  26,  25,  15,  10,
    #         13,  10,  17,  23,  17,  16,   0,   7,
    #         14,  25,  24,  15,   8,  25,  20,  15,
    #         19,  20,  11,   6,   7,   6,  20,  16,
    #         -7,   2, -15, -12, -14, -15, -10, -10),
    # 'R': (  35,  29,  33,   4,  37,  33,  56,  50,
    #         55,  29,  56,  67,  55,  62,  34,  60,
    #         19,  35,  28,  33,  45,  27,  25,  15,
    #          0,   5,  16,  13,  18,  -4,  -9,  -6,
    #        -28, -35, -16, -21, -13, -29, -46, -30,
    #        -42, -28, -42, -25, -25, -35, -26, -46,
    #        -53, -38, -31, -26, -29, -43, -44, -53,
    #        -30, -24, -18,   5,  -2, -18, -31, -32),
    # 'Q': (   6,   1,  -8,-104,  69,  24,  88,  26,
    #         14,  32,  60, -10,  20,  76,  57,  24,
    #         -2,  43,  32,  60,  72,  63,  43,   2,
    #          1, -16,  22,  17,  25,  20, -13,  -6,
    #        -14, -15,  -2,  -5,  -1, -10, -20, -22,
    #        -30,  -6, -13, -11, -16, -11, -16, -27,
    #        -36, -18,   0, -19, -15, -15, -21, -38,
    #        -39, -30, -31, -13, -31, -36, -34, -42),
    # 'K': (   4,  54,  47, -99, -99,  60,  83, -62,
    #        -32,  10,  55,  56,  56,  55,  10,   3,
    #        -62,  12, -57,  44, -67,  28,  37, -31,
    #        -55,  50,  11,  -4, -19,  13,   0, -49,
    #        -55, -43, -52, -28, -51, -47,  -8, -50,
    #        -47, -42, -43, -79, -64, -32, -29, -32,
    #         -4,   3, -14, -50, -57, -18,  13,   4,
    #         17,  30,  -3, -14,   6,  -1,  40,  18),
}

for k, table in pst.items():
    padrow = lambda row: (0,) + tuple(x+piece[k] for x in row) + (0,)
    pst[k] = sum((padrow(table[i*8:i*8+8]) for i in range(8)), ())
    pst[k] = (0,)*20 + pst[k] + (0,)*20
#used for mate value
MATE_LOWER = piece['K'] - 10*piece['Q']
MATE_UPPER = piece['K'] + 10*piece['Q']

class DecisionTreeAI(player.Player):
    def __init__(self, description="Chess player that uses a decision tree.", color=chess.WHITE, depth=3, random=False,
                 epsilon=0, sunfish=False, offensive=True, defensive=True):
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
        self.fish = sunfish

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
        # print(numLegalMoves)
        for i in range(0, numLegalMoves):
            tempBoard = chess.Board(board.fen())
            tempBoard.push(legalMoves[i])
            if self.randomOpponent:
                score = self.traverseExpectimaxTree(tempBoard, self.depth)
            else:
                score = self.traverseMinimaxTree(current_move=legalMoves[i], board=tempBoard, depth=self.depth, isMax=False)
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
        return legalMoves[bestMoves[int(randMove)]]

    # '''
    # def stockfish_evaluation(self, board=chess.Board(), depth_limit=1, time_limit=0.01):
    #     engine = chess.engine.SimpleEngine.popen_uci(
    #         r"C:\Users\Nedan\Documents\02465students\ChessEngine\stockfish_13_win_x64_bmi2\stockfish_13_win_x64_bmi2")
    #     score = engine.analyse(board, chess.engine.Limit(depth=depth_limit, time=time_limit))
    #     if chess.Color() == True:
    #         if score['score'].white.score() is None:
    #             return score['score'].white().mate()
    #         else:
    #             return score['score'].white().score()
    #     else:
    #         if score['score'].black().score() is None:
    #             return score['score'].black().mate()
    #         else:
    #             return score['score'].black().score()'''

    def fen2iboard(self, board=chess.Board()):
        temp_board = board.fen()
        temp_fen_board  = temp_board.split(" ")
        fen_board = temp_fen_board[0]
        # replace each number with corresponding number of spaces
        f = lambda x: "".join(["." * int(k) if (k in "12345678") else k for k in x])
        # split on /
        # end each line with \n and append space at beginning
        return ([f(" " + s + '\n') for s in fen_board.split("/")])

    def iboard2sunfish(self, iboard):
        edge_buffer = "         \n"
        return (''.join([edge_buffer, edge_buffer, "".join(iboard), edge_buffer, edge_buffer[:-1]]))

    def fen2sunfish(self, board=chess.Board()):
        iboard = self.fen2iboard(board)
        return self.iboard2sunfish(iboard)

    #sunfish evaluates a certain action, and not the board-state
    def sunfish_evaluation(self, current_move, board=chess.Board()):
        temp_board=self.fen2sunfish(board)
        x = current_move.uci()[:2]
        y = current_move.uci()[2:]

        i, j = self.position2pst(x), self.position2pst(y)
        z, u = self.position2digit(x), self.position2digit(y)
        p, q = temp_board[u], temp_board[z]
        p = p.capitalize()
        # Actual move
        #score1 = (pst[p][j] - pst[p][i])/10
        score = pst[p][j] - pst[p][i]
        # Capture
        # if q.islower():
        #     score += pst[q.upper()][119 - j]
        ''' # Castling check detection
        if abs(j - self.kp) < 2:
            score += pst['K'][119 - j]'''
        # Castling
        # if p == 'K' and abs(i - j) == 2:
        #     score += pst['R'][(i + j) // 2]
        #     score -= pst['R'][A1 if j < i else H1]
        # Special pawn stuff
        # if p == 'P':
        #     if A8 <= j <= H8:
        #         score += pst['Q'][j] - pst['P'][j]
            #if j == self.ep:
                #score += pst['P'][119 - (j + S)]
        #print(score)
        #material
        score += (1 * (len(board.pieces(chess.PAWN, self.color)) - len(board.pieces(chess.PAWN, not self.color))) +
                         3 * (len(board.pieces(chess.BISHOP, self.color)) - len(
                         board.pieces(chess.BISHOP, not self.color))) +
                         3 * (len(board.pieces(chess.KNIGHT, self.color)) - len(
                            board.pieces(chess.KNIGHT, not self.color))) +
                         5 * (len(board.pieces(chess.ROOK, self.color)) - len(board.pieces(chess.ROOK, not self.color))) +
                         9 * (len(board.pieces(chess.QUEEN, self.color)) - len(board.pieces(chess.QUEEN, not self.color))))
                #          10 * (len(board.pieces(chess.KING, self.color)) - len(board.pieces(chess.KING, not self.color))))
        #if self.color == chess.WHITE:
            #if q.islower():
        #        score += (pst[q.upper()][119 - j])
        #else:
        #    if q.isupper():
        #        score += (pst[q][119-j])
        # Castling check detection
        # Castling
        #if p == 'K' and abs(i-j) == 2:
        #    score += pst['R'][(i+j)//2]
        #    score -= pst['R'][A1 if j < i else H1]
        # Special pawn stuff

        #score2 = self.evaluateBoard(board)
        #score = score1+score2
        #print(score)
        return score

    def evaluateBoard(self, board=chess.Board()):

        score = (1 * (len(board.pieces(chess.PAWN, self.color)) - len(board.pieces(chess.PAWN, not self.color))) +
                 3 * (len(board.pieces(chess.BISHOP, self.color)) - len(
                    board.pieces(chess.BISHOP, not self.color))) +
                 3 * (len(board.pieces(chess.KNIGHT, self.color)) - len(
                    board.pieces(chess.KNIGHT, not self.color))) +
                 5 * (len(board.pieces(chess.ROOK, self.color)) - len(board.pieces(chess.ROOK, not self.color))) +
                 10 * (len(board.pieces(chess.QUEEN, self.color)) - len(board.pieces(chess.QUEEN, not self.color))))
                 #100 * (len(board.pieces(chess.KING, self.color)) - len(board.pieces(chess.KING, not self.color))))

        # mobility = 0.1 * len(board.legal_moves)
        return score

    def traverseMinimaxTree(self,current_move, board=chess.Board(), depth=0, isMax=True, alpha=float('-inf'), beta=float('inf')):

        legalMoves = list(board.legal_moves)
        if depth == 0 or len(legalMoves) == 0:
            if self.fish:
                score = self.sunfish_evaluation(current_move=current_move, board=board)
            else:
                score = self.evaluateBoard(board)
            self.count += 1
            # if self.fish:
            #     if not isMax and self.offensive:
            #         if board.is_check():
            #             score += 16
            #         if board.is_checkmate():
            #             score += 5000
            #     elif self.defensive:
            #         if board.is_check():
            #             score -= 16
            #         if board.is_checkmate():
            #             score -= 5000
            # else:
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
                # print(alpha, beta)
                if self.randomOpponent:
                    score = self.traverseExpectimaxTree(tempBoard, depth - 1)
                else:
                    score = self.traverseMinimaxTree(current_move=legalMoves[i], board=tempBoard, depth=depth - 1, isMax=False, alpha=alpha, beta=beta)
                    # score = score.white().score
                if minimaxScore < score:
                    minimaxScore = score
                alpha = max(alpha, score)
                if beta <= alpha:
                    self.prunecount += 1
                    #    print('white')
                    break
            else:
                # print(alpha, beta)
                score = self.traverseMinimaxTree(current_move=legalMoves[i], board=tempBoard, depth=depth - 1, isMax=True, alpha=alpha, beta=beta)
                # score = score.white().score
                if minimaxScore > score:
                    minimaxScore = score

                beta = min(beta, score)
                if beta <= alpha:
                    # print('black')
                    self.prunecount += 1
                    break
        return minimaxScore

    def traverseExpectimaxTree(self, board=chess.Board(), depth=0):
        legalMoves = list(board.legal_moves)
        if depth == 0 or len(legalMoves) == 0:
            score = self.evaluateBoard(board)
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

    def position2pst(self, position):
        digit = 0
        if position[0] == 'a':
            digit += 0
        if position[0] == 'b':
            digit += 1
        if position[0] == 'c':
            digit += 2
        if position[0] == 'd':
            digit += 3
        if position[0] == 'e':
            digit += 4
        if position[0] == 'f':
            digit += 5
        if position[0] == 'g':
            digit += 6
        if position[0] == 'h':
            digit += 7

        if position[1] == '1':
            digit += 56
        if position[1] == '2':
            digit += 48
        if position[1] == '3':
            digit += 40
        if position[1] == '4':
            digit += 32
        if position[1] == '5':
            digit += 24
        if position[1] == '6':
            digit += 16
        if position[1] == '7':
            digit += 8
        if position[1] == '8':
            digit += 0
        return digit

    def position2digit(self, position):
        digit = 0
        if position[0] == 'a':
            digit += 1
        if position[0] == 'b':
            digit += 2
        if position[0] == 'c':
            digit += 3
        if position[0] == 'd':
            digit += 4
        if position[0] == 'e':
            digit += 5
        if position[0] == 'f':
            digit += 6
        if position[0] == 'g':
            digit += 7
        if position[0] == 'h':
            digit += 8

        if position[1] == '1':
            digit += 90
        if position[1] == '2':
            digit += 80
        if position[1] == '3':
            digit += 70
        if position[1] == '4':
            digit += 60
        if position[1] == '5':
            digit += 50
        if position[1] == '6':
            digit += 40
        if position[1] == '7':
            digit += 30
        if position[1] == '8':
            digit += 20
        return digit

print()