# Chess Playground

Goal: This will be a chess engine that will use Machine learning to play chess at different levels. The playground is for me to play around with different algorithsms and settings
Uses the python-chess library to take care of the chess part (legal moves, number of pieces, etc)

Currently, the following algorithms have been implemented. They all use class inheritance from the same Player base class to be easily playable against each other

### Human Player
Allows the human to play

### Random Player
Literally plays random moves out of its allowed ones

### Decision Trees
Uses a Minimax search to look forward in moves and select the best move it evaluates. The algorithm can be customised to search different depths (how many plys it looks forwards), to be offensive (to actively seek to check the opponent) or defensive (to actively avoid checks), to be a minimax or expectimax algorithm, to have a chance of randomly selecting a move (epsilon-minimax).
The minimax algorithm assumes the opponent will select the best move for them, while the expectimax algorithm takes the average and would theoretically play better against an opponent with some randomness.

The following evaluation function is used for the leaves

```python
1 * (len(board.pieces(chess.PAWN, self.color)) - len(board.pieces(chess.PAWN, not self.color))) +
3 * (len(board.pieces(chess.BISHOP, self.color)) - len(board.pieces(chess.BISHOP, not self.color))) +
3 * (len(board.pieces(chess.KNIGHT, self.color)) - len(board.pieces(chess.KNIGHT, not self.color))) +
5 * (len(board.pieces(chess.ROOK, self.color)) - len(board.pieces(chess.ROOK, not self.color))) +
9 * (len(board.pieces(chess.QUEEN, self.color)) - len(board.pieces(chess.QUEEN, not self.color))) +
100 * (len(board.pieces(chess.KING, self.color)) - len(board.pieces(chess.KING, not self.color)))
```

Optionally, when offensive or defensive, the following is added or subtracted, respectively, from the score
```python
if isMinNode and self.offensive:
    if board.is_check():
        score += 50
    if board.is_checkmate():
        score += 5000
elif self.defensive:
    if board.is_check():
        score -= 50
    if board.is_checkmate():
score -= 5000
```

Most runs were tested with depth 3. Detailed info in the stats folder
* The **minimax** and **expectimax** algorithms, when **offensive**, consistently beat the random AI.
* A minimax algorithm against itself wins an equal amount of games as it loses, while a offensive algorithm consistently draws against a defensive one.
  * A **defensive-only** minimax algorithm can win against a random AI, but tends to draw a game more (which can be expected since it's not actively seeking to beat the opponent)
  * A **depth 3** minimax always beats a **depth 2**, showing that going deeper is a clear advantage. 
* The minimax algorithm almost always beats the expectimax algorithm, which is expected.
  * Adding randomness to minimax (20% change move is randomly selected, a sort-of epsilon-minimax), the expectimax has the advantage and starts winning most games. A regular minimax is more prone to draw in this case. If the randomness factor is only 10%, expectimax starts losing again. This is also expected, since a game with only 30-40 plys on average, doing 3-4 random moves shouldn't affect it much

Unfortunately, I was not able to go past depth 3 since the algorithm takes considerably longer to run at depth 4 and above (a game in depth 3 run in a few (5-10) minutes, depth 5 didn't finish after hours on a GPU in Google colab). Other than being limited to depth 3, even with that depth, the algorithm is slow to play and not very realistic against an opponent in real time.

### Scikit AI
Uses supervised learning to learn to play chess
data: http://chessok.com/?page_id=694, http://www.chess-poster.com/english/pgn/pgn_files.htm#K
Need to more testing to evaluate if it actually works and compare against the others

### Deep Reinforcement Learning
Next big step