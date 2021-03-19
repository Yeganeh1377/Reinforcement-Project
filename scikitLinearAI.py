import chess
import chess.pgn
import random
import player
import decisionTreeAI
import joblib
from sklearn import linear_model

class ScikitLinearAI(decisionTreeAI.DecisionTreeAI):
    def __init__(self, description = "Chess player that does random moves.", color = chess.WHITE, depth = 3, random = False, retrain = False):
        self.type = "AI"
        self.description = description
        self.color = color
        self.depth = depth
        self.randomOpponent = random

        if (retrain):
            self.classifier = linear_model.SGDRegressor()
            X, y = self.readFile("data/Kasparov.pgn");
            print("Done reading data")
            self.classifier.fit(X, y)
            joblib.dump(self.classifier, "data/SGDRegressorModel_Kasparov.pkl")
            print("Done fitting data")
        self.classifier = joblib.load('data/SGDRegressorModel_Kasparov.pkl')

    def evaluateBoard(self, board=chess.Board()):
        return self.classifier.predict([self.getFeaturesFromBoard(board)])[0]

    def readFile(self, fileName):
        pgn = open(fileName)
        X = []
        y = []

        while True:
            game = chess.pgn.read_game(pgn)
            if not game:
                break

            result = 0
            if game.headers["Result"] == "1-0":
                if self.color == chess.WHITE:
                    result = 1
                else:
                    result = -1
            elif game.headers["Result"] == "0-1":
                if self.color == chess.BLACK:
                    result = 1
                else:
                    result = -1

            board = game.board()
            for move in game.main_line():
                board.push(move)
                X.append(self.getFeaturesFromBoard(board))
                y.append(result)

        return X, y

    def getFeaturesFromBoard(self, board = chess.Board()):
        x = []
        for square in range(0, 64):
            curPiece = board.piece_at(square)
            for pieceType in range(1, 13):
                if curPiece and curPiece.color:
                    colorOffset = 0
                else:
                    colorOffset = 6
                if curPiece and curPiece.piece_type + colorOffset == pieceType:
                    x.append(1)
                else:
                    x.append(0)
            x.append(int(board.turn))
        return x