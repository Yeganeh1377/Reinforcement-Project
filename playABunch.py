from play import play
import chess
import numpy as np

def playABunch(numGames, printGame=False):
    player1Wins = 0
    player2Wins = 0
    draws = 0
    totalMoves = []

    for i in range(1, numGames + 1):
        print("Starting game", i)
        finalBoard = play(printGame)
        if (finalBoard.result() == '1-0'):
            player1Wins += 1
            print('Player 1 wins game', i, 'in', finalBoard.fullmove_number, 'moves.')
            print(finalBoard)
            print('\n')
        elif (finalBoard.result() == '0-1'):
            player2Wins += 1
            print('Player 2 wins game', i, 'in', finalBoard.fullmove_number, 'moves.')
            print(finalBoard)
            print('\n')
        elif (finalBoard.result() == '1/2-1/2'):
            draws += 1
            print('Draw in game', i, 'in', finalBoard.fullmove_number, 'moves.')
            print(finalBoard)
            print('\n')
        totalMoves.append(finalBoard.fullmove_number)

    print('\nPlayer 1 wins', player1Wins, 'game(s).\nPlayer 2 wins', player2Wins, 'game(s).\nDraw(s)', draws, 'games(s).\nAVG Moves ', np.sum(totalMoves)/numGames)

if __name__ == '__main__':
    nGames = input("How many games? ")
    printGame = input("Print games? (Yes or No) ")
    playABunch(int(nGames), printGame == 'Yes')
