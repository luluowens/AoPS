'''For your homework during the final 2 weeks of the course,
you'll write a Python program to implement the 2-player game of Checkers.

Checkers is played on an 8-by-8 checkerboard with squares of alternating colors,
as shown below:
(I used the colors 'dark green' and 'blanched almond' for the board,
and 'red' and 'white' for the players. These colors are pretty close to the
standard American checkers colors. But you can use any colors you want.)

Only the dark squares of the board are used. Each player starts with 12 pieces,
with one piece on each dark square of the first 3 rows of either side of the checkerboard,
as shown above. The player with the red pieces goes first, and the players alternate turns.

On a player's turn, the player must move one of his pieces, using either of the rules below:

1. A piece may be moved forward to an empty diagonally-adjacent square.
For red, "forward" is from top-to-bottom on the board; for white, "forward"
is from bottom-to-top.

2. A piece may jump a piece of the other player. A jump can be made if an
opponent's piece is in a square that the current player's piece could move to
if the square were empty, and if the square immediately beyond the opponent's piece
(continuing in a straight line) is empty. The player moves his piece to the empty square
beyond the opponent's piece, and removes the opponent's piece from the board.

Important: if the player is able to make a jump, they must do so.
(If the player has more than one jumping move to choose from,
they may choose whichever one they like.) In addition, the piece that has
just jumped may make additional jumps on the same turn, and in fact it must do so.
That is, the piece must continue jumping until it has no more jumps available,
or until it becomes a new king (see below).

If a piece reaches the last row of the board (that is, the bottom row for red or
the top row for white), it immediately becomes a king. (We indicate a king by
putting a star on top of the piece.) A piece becoming a king ends the player's turn,
even if the king was made via a jump and is still able to jump.
Kings can move and jump forwards or backwards.

If a player has no legal move on their turn, their opponent wins the game.
This can occur if the player runs out of pieces, or if the player's pieces all
become "blocked" and have no empty squares to legally move or jump to.
A game can also end in a draw if both players agree that neither of them can manage to win.

The animation below shows the first few moves of a sample game.
(Red is playing rather badly in this game.) Notice the double-jump that
white makes a few moves in, and that a bit later white makes one of their pieces into a king.
'''

from tkinter import *
from tkinter import messagebox

class CheckersSquare(Canvas):
    def __init__(self,master,row,col) :
        '''CheckersSquare(master,row,col)
        creates a new blank Checkers square at coordinate (row, col)'''
        # create and place the widget
        if (row + col) % 2 == 0 :
            Canvas.__init__(self,master,width=50,height=50,bg='dark green')
        else :
            Canvas.__init__(self,master,width=50,height=50,bg='blanched almond')
        self.grid(row,col)
        # set the attributes
        self.position = (row, col)
        # bind button click to placing a piece
        self.bind('',master.get_click)
    


class CheckersBoard:
    '''represents a board for the Checkers game'''

    def __init__(self):
        '''CheckersBoard()
        creates a CheckersBoard in starting position'''
        self.board = {}  # dict to store position of checkers
        # create starting position
        for row in range(8):
            for col in range(8):
                coords = (row,col)
                if row > 4 :
                    if (row + col) % 2 == 0 :
                        self.board[coords] = 0  # player 0 for red
                elif row < 4 :
                    if (row + col) % 2 == 0 :
                        self.board[coords] = 1  # player 1 for white
                else:
                    self.board[coords] = None  # empty
        self.currentPlayer = 0  # player 0 (red) starts

    def get_piece(self,coords):
        '''CheckersBoard.get_piece(coords) -> int
        returns the piece at coords'''
        return self.board[coords]

    def get_player(self):
        '''CheckersBoard.get_player() -> int
        returns the current player'''
        return self.currentPlayer