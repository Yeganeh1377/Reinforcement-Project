import chess
import human
import randomAI

def play(printGame = True):
    board = chess.Board()

    if printGame:
        print board
        print "Let's start with this game of chess"

    numMoves = 0
    #player1 = human.Human("Player 1")
    player1 = randomAI.RandomAI("Player 1")
    player2 = randomAI.RandomAI("Player 2")

    while (not board.is_game_over()):

        if printGame:
            print '\n', player1.description, 'will now play'

        player1Move = player1.move(board)
        board.push(player1Move)

        if printGame:
            print board

        if printGame:
            print '\n', player2.description, 'will now play'

        player2Move = player2.move(board)
        if player2Move == -1:
            return board, numMoves
        board.push(player2Move)

        if printGame:
            print board

        numMoves += 1

    if printGame:
        print '\nResult:', board.result()
        print 'Number of moves:', numMoves

    return board, numMoves


if __name__ == '__main__':
    play()