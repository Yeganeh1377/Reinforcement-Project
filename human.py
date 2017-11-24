import chess
import player

class Human(player.Player):
    def __init__(self, description = "Human chess player."):
        self.type = "Human"
        self.description = description

    def move(self, board):
        legalMoves = list(board.legal_moves)

        userMove = 0
        while (not userMove):
            try:
                userInput = raw_input('Please enter a valid move! ')
                userMove = chess.Move.from_uci(userInput)
            except ValueError as ve:
                print 'That was not a chess move;', ve

        while (not userMove in legalMoves):
            userInput = raw_input("That move won't work on this board. Try again. ")
            userMove = chess.Move.from_uci(userInput)

        return userMove