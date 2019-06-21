import chess
import human
import randomAI
import decisionTreeAI
import scikitLinearAI

def play(printGame = True):
    board = chess.Board()

    if printGame:
        print(board)
        print("Let's start with this game of chess")

    # player1 = human.Human("Player 1")
    # player1 = randomAI.RandomAI("Player 1")
    player1 = decisionTreeAI.DecisionTreeAI("Player 1", chess.WHITE, 3)
    player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3)
    # player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3, False, 0.2)
    # player1 = decisionTreeAI.DecisionTreeAI("Player 1", chess.WHITE, 3, False, 0, True, False)
    # player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3, False, 0, False, True)
    # player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3, True)
    # player2 = scikitLinearAI.ScikitLinearAI("Player 2", chess.BLACK, 1, True)

    while (not board.is_game_over()):

        if printGame:
            print('\n', player1.description, 'will now play')

        player1Move = player1.move(board)
        board.push(player1Move)

        if printGame:
            print(board)

        if printGame:
            print('\n', player2.description, 'will now play')

        player2Move = player2.move(board)
        if player2Move == -1:
            if printGame:
                print('\nResult:', board.result())
                print('Number of plys:', board.fullmove_number)
            return board
        board.push(player2Move)

        if printGame:
            print(board)

    if printGame:
        print('\nResult:', board.result())
        print('Number of plys:', board.fullmove_number)

    return board


if __name__ == '__main__':
    play()