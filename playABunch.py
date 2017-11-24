from play import play
import chess

def playABunch(numGames):
    player1Wins = 0
    player2Wins = 0
    draws = 0

    for i in range(1, numGames + 1):
        finalBoard, numMoves = play(False)
        if (finalBoard.result() == '1-0'):
            player1Wins += 1
            print 'Player 1 wins game', i, 'in', numMoves, 'moves.'
            print finalBoard
            print '\n'
        elif (finalBoard.result() == '0-1'):
            player2Wins += 1
            print 'Player 2 wins game', i, 'in', numMoves, 'moves.'
            print finalBoard
            print '\n'
        elif (finalBoard.result() == '1/2-1/2'):
            draws += 1

    print '\nPlayer 1 wins', player1Wins, 'game(s).\nPlayer 2 wins', player2Wins, 'game(s).\nDraw(s)', draws

if __name__ == '__main__':
    nGames = raw_input("How many games? ")
    playABunch(int(nGames))