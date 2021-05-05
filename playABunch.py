from play import play
import chess
import numpy as np
from elosports.elo import Elo
import time

def playABunch(numGames, player1, player2, printGame=False):
    player1Wins = 0
    player2Wins = 0
    draws = 0
    totalMoves = []

    '''eloLeague = Elo(k=20)
    eloLeague.addPlayer(player1)
    eloLeague.addPlayer(player2)
    eloLeague.expectResult(eloLeague.ratingDict[player1], eloLeague.ratingDict[player2])
    '''
    for i in range(1, numGames + 1):
        print("Starting game", i)
        finalBoard = play(printGame)
        if (finalBoard.result() == '1-0'):
            player1Wins += 1
            #eloLeague.gameOver(winner=player1, loser = player2, winnerHome=0)

            print('Player 1 wins game', i, 'in', finalBoard.fullmove_number, 'moves.')
            print(finalBoard)
            print('\n')
        elif (finalBoard.result() == '0-1'):
            player2Wins += 1
            #eloLeague.gameOver(winner=player2, loser=player1, winnerHome=0)
            print('Player 2 wins game', i, 'in', finalBoard.fullmove_number, 'moves.')
            print(finalBoard)
            print('\n')
        elif (finalBoard.result() == '1/2-1/2'):
            draws += 1
            print('Draw in game', i, 'in', finalBoard.fullmove_number, 'moves.')
            print(finalBoard)
            print('\n')
        totalMoves.append(finalBoard.fullmove_number)
        #print(eloLeague.ratingDict)

    print('\nPlayer 1 wins', player1Wins, 'game(s).\nPlayer 2 wins', player2Wins, 'game(s).\nDraw(s)', draws,'games(s)')
    print('\nAVG Moves ', np.sum(totalMoves) / numGames, '\nConfidence interval ', 1.96 * np.std(totalMoves) / np.sqrt(numGames))


if __name__ == '__main__':
    nGames = input("How many games? ")
    printGame = input("Print games? (Yes or No) ")
    playABunch(int(nGames), 'minimax', 'random', printGame == 'Yes')
print()