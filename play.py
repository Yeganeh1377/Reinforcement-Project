import chess
import human
import randomAI
import decisionTreeAI
import decisionTreeAISunfish
import scikitLinearAI
import time
import numpy as np

def play(printGame = True):
    #board = chess.Board()
    board = chess.Board()
    if printGame:
        print(board)
        print("Let's start with this game of chess")

    # player1 = human.Human("Player 1")
    #player2 = randomAI.RandomAI("Player 2")
    #player1 = decisionTreeAI.DecisionTreeAI("Player 1", chess.WHITE, 3)
    player2 = decisionTreeAISunfish.DecisionTreeAI("Player 2", chess.BLACK, depth = 1, random= False, sunfish=True)
    player1 = decisionTreeAI.DecisionTreeAI("Player 1", chess.WHITE, depth = 1, random = False) #random false is minimax
    # player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3, False, 0.2)
    # player1 = decisionTreeAI.DecisionTreeAI("Player 1", chess.WHITE, 3, False, 0, True, False)
    # player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3, False, 0, False, True)
    # player2 = decisionTreeAI.DecisionTreeAI("Player 2", chess.BLACK, 3, True)
    #player2 = scikitLinearAI.ScikitLinearAI("Player 2", chess.BLACK, 1, True)
    '''starts1 = []
    starts2 = []
    ends1 = []
    ends2 = []'''

    while (not board.is_game_over()):
        # starting time
        ''' start1 = time.time()
        starts1 = np.append(starts1, start1)'''

        if printGame:
            print('\n', player1.description, 'will now play')

        player1Move = player1.move(board)
        board.push(player1Move)
        '''
        time.sleep(1)
        end1 = time.time()
        ends1 = np.append(ends1, end1)
        '''

        if printGame:
            print(board)

        if printGame:
            print('\n', player2.description, 'will now play')

        ''' 
        start2 = time.time()
        starts2 = np.append(starts2, start2)'''

        player2Move = player2.move(board)
        '''time.sleep(1)
        end2 = time.time()
        ends2 = np.append(ends2, end2)'''

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
#, starts1, starts2, ends1, ends2


if __name__ == '__main__':
    board = play()

print()