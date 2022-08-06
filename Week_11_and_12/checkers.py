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
        if (row + col) % 2 == 1 :
            Canvas.__init__(self,master,width=50,height=50,bg='dark green')
        else :
            Canvas.__init__(self,master,width=50,height=50,bg='blanched almond')
        self.grid(row = row,column = col)
        # set the attributes
        self.position = (row, col)
        self.color = "red"
        self.king = False
        # bind button click to placing a piece
        self.bind('<Button-1>', master.get_click)

    def get_position(self):
        '''CheckersSquare.get_position() -> (int,int)
        returns (row,column) of square'''
        return self.position

    def remove_checker(self) :
        '''CheckersSquare.remove_checker()
        removes all checkers from the square
        '''
        checkers = self.find_all()
        for checker in checkers :
            self.delete(checker)

    def place_checker(self, color) :
        '''CheckersSquare.place_checker(color)
        changes color of piece on square to specified color'''
        # removes any existing checkers from square
        checkers = self.find_all()
        for checker in checkers :
            self.delete(checker)
        self.create_oval(10,10,44,44,fill=color)

    def select_checker(self) :
        '''CheckersSquare.select_checker()
        highlights the square with a black boarder
        '''
        self.configure(highlightthickness = 3)
        self.configure(highlightbackground = 'black')
    
    def deselect_checker(self) :
        '''CheckersSquare.select_checker()
        undoes the highlight for the square
        '''
        if (self.position[0] + self.position[1]) % 2 == 1 :
            self.configure(highlightbackground = 'dark green')
        else :
            self.configure(highlightbackground = 'blanched almond')

    def make_king(self) :
        '''CheckersSquare.make_king()
        makes the checker a king
        '''
        self.king = True
        self.create_text(28, 38, text="*", fill="black", font=('Arial 50'))


class CheckersBoard :
    '''represents a board for the Checkers game'''

    def __init__(self) :
        '''CheckersBoard()
        creates a CheckersBoard in starting position'''
        self.board = {}  # dict to store position of checkers
        # create starting position
        for row in range(8):
            for col in range(8):
                coords = (row,col)
                if row < 3 :
                    if (row + col) % 2 == 1 :
                        self.board[coords] = 0  # player 0 for red
                    else :
                        self.board[coords] = -1 # empty
                elif row > 4 :
                    if (row + col) % 2 == 1 :
                        self.board[coords] = 1  # player 1 for white
                    else :
                        self.board[coords] = -1  # empty
                else:
                    self.board[coords] = -1  # empty
        # player 0 (red) starts
        self.currentPlayer = 0
        # keeps track of if a player needs to jump again
        self.new_coords = (0,0)
        self.jump = False

    def get_piece(self,coords) :
        '''CheckersBoard.get_piece(coords) -> int
        returns the piece at coords'''
        return self.board[coords]

    def get_player(self) :
        '''CheckersBoard.get_player() -> int
        returns the current player'''
        return self.currentPlayer

    def get_jump_again(self) :
        '''CheckersBoard.get_jump_again() -> bool
        returns the jump again status'''
        return self.jump_again

    def set_jump_again(self, val) :
        '''CheckersBoard.set_jump_again(val)
        sets the jump again status'''
        self.jump_again = val

    def get_row(self, row) :
        '''CheckersBoard.get_row(row)
        returns the row in the board
        '''
        row_squares = []
        for element in self.board :
            if element[0] == row :
                row_squares.append([element, self.board[element]])
        return row_squares

    def change_player(self) :
        '''CheckersBoard.change_player()
        changes the player to the other player
        '''
        self.currentPlayer = 1 - self.currentPlayer

    def is_legal_move(self,old_pos,new_pos) :
        '''CheckersBoard.is_legal_move(old_pos, new_pos) -> boolean
        returns a boolean for is the player's move is legal'''
        # check if the jump is legal
        if self.is_legal_jump(old_pos, new_pos) :
            self.jump = True
            return True
        elif self.currentPlayer == 0 :
            self.jump = False
            # check if space is empty and next posititon is 1 away (only backward)
            return (new_pos[0] - old_pos[0] == 1 and abs(new_pos[1] - old_pos[1]) == 1 and self.board[new_pos] == -1)
        elif self.currentPlayer == 1 :
            self.jump = False
            # check if space is empty and next posititon is 1 away (only forward)
            return (old_pos[0] - new_pos[0] == 1 and abs(old_pos[1] - new_pos[1]) == 1 and self.board[new_pos] == -1)

    def is_legal_king(self, old_pos, new_pos) :
        if self.is_legal_king_jump(old_pos, new_pos) :
            self.jump = True
            return True
        else :
            self.jump = False
            # check if space is empty and next posititon is 1 away (only forward)
            return (abs(old_pos[0] - new_pos[0]) == 1 and abs(old_pos[1] - new_pos[1]) == 1 and self.board[new_pos] == -1)

    def is_legal_jump(self, old_pos, new_pos) :
        '''CheckersBoard.is_legal_jump(old_pos, new_pos) -> boolean
        checks to see if the jump is legal
        returns a boolean
        '''
        if self.currentPlayer == 0 :
            if (new_pos[0] - old_pos[0] == 2 and abs(new_pos[1] - old_pos[1]) == 2 and self.board[new_pos] == -1) :
                mid_square = ((old_pos[0] + new_pos[0]) // 2, (old_pos[1] + new_pos[1]) // 2)
                if self.board[mid_square] == 1 - self.currentPlayer :
                    self.board[mid_square] = -1
                    return True
        elif self.currentPlayer == 1 :
            if (old_pos[0] - new_pos[0] == 2 and abs(old_pos[1] - new_pos[1]) == 2 and self.board[new_pos] == -1) :
                mid_square = ((old_pos[0] + new_pos[0]) // 2, (old_pos[1] + new_pos[1]) // 2)
                if self.board[mid_square] == 1 - self.currentPlayer :
                    self.board[mid_square] = -1
                    return True
        return False

    def is_legal_king_jump(self, old_pos, new_pos) :
        if (abs(old_pos[0] - new_pos[0]) == 2 and abs(old_pos[1] - new_pos[1]) == 2 and self.board[new_pos] == -1) :
            mid_square = ((old_pos[0] + new_pos[0]) // 2, (old_pos[1] + new_pos[1]) // 2)
            if self.board[mid_square] == 1 - self.currentPlayer :
                self.board[mid_square] = -1
                return True
        return False

    def check_possible_jumps(self, curr_pos) :
        '''CheckersBoard.check_possible_jumps(curr_pos)
        checks to see if the checker can jump again
        returns if the checker can jump again
        '''
        # seeing if the player is red or white
        # player is red
        if self.currentPlayer == 0 :
            if curr_pos[0] + 2 >= 0 and curr_pos[0] + 2 <= 7 and curr_pos[1] + 2 >= 0 and curr_pos[1] + 2 <= 7 :
                position_1 = (curr_pos[0] + 1, curr_pos[1] + 1)
                new_pos_1 = (curr_pos[0] + 2, curr_pos[1] + 2)
                if self.board[position_1] == 1 and self.board[new_pos_1] == -1 :
                    self.new_coords = new_pos_1
                    self.jump_again = True
                    return True
                if curr_pos[1] - 2 >= 0 and curr_pos[1] - 2 <= 7 :
                    position_2 = (curr_pos[0] + 1, curr_pos[1] - 1)
                    new_pos_2 = (curr_pos[0] + 2, curr_pos[1] - 2)
                    if self.board[position_2] == 1 and self.board[new_pos_2] == -1 :
                        self.new_coords = new_pos_2
                        self.jump_again = True
                        return True
        # player is white
        elif self.currentPlayer == 1 :
            if curr_pos[0] - 2 >= 0 and curr_pos[0] - 2 <= 7 and curr_pos[1] + 2 >= 0 and curr_pos[1] + 2 <= 7 :
                position_1 = (curr_pos[0] - 1, curr_pos[1] + 1)
                new_pos_1 = (curr_pos[0] - 2, curr_pos[1] + 2)
                if self.board[position_1] == 0 and self.board[new_pos_1] == -1 :
                    self.new_coords = new_pos_1
                    self.jump_again = True
                    return True
                if curr_pos[1] - 2 >= 0 and curr_pos[1] - 2 <= 7 :
                    position_2 = (curr_pos[0] - 1, curr_pos[1] - 1)
                    new_pos_2 = (curr_pos[0] - 2, curr_pos[1] - 2)
                    if self.board[position_2] == 0 and self.board[new_pos_2] == -1 :
                        self.new_coords = new_pos_2
                        self.jump_again = True
                        return True
        # if no position was returned, return False
        self.jump_again = False
        return False

    def move_checker(self, old_pos, new_pos) :
        '''CheckersBoard.move_checker(old_pos, new_pos)
        moves the checker from one square to another
        '''
        if abs(old_pos[0] - new_pos[0]) == 2 and abs(old_pos[1] - new_pos[1]) == 2 :
            mid_square = ((old_pos[0] + new_pos[0]) // 2, (old_pos[1] + new_pos[1]) // 2)
            self.board[mid_square] = -1
        self.board[old_pos] = -1
        self.board[new_pos] = self.currentPlayer



class CheckersGame(Frame) :
    '''represents a Checkers game'''

    def __init__(self,master) :
        '''CheckersGame(master)
        creates a new Checkers game'''
        # initialize the Frame
        Frame.__init__(self,master,bg='white')
        self.grid()
        # set up game data
        self.colors = ('red','white')  # players' colors
        # create board in starting position, player 0 going first
        self.board = CheckersBoard()
        self.squares = {}  # stores CheckersSquares
        for row in range(8) :
            for column in range(8) :
                rc = (row,column)
                self.squares[rc] = CheckersSquare(self,row,column)
        # set up status markers
        self.rowconfigure(8,minsize=1)  # leave a little space
        # create turn indicator square
        self.turnSquare = CheckersSquare(self,9,2)
        # set background to light gray instead of almond or green
        self.turnSquare.configure(bg='light gray')
        # set color of checkers piece on the square
        self.turnSquare.place_checker(self.colors[0])
        self.turnSquare.configure(highlightbackground='light gray')
        self.turnSquare.unbind('')
        # set up Turn label
        self.turnLabel = Label(self,text='Turn: ',font=('Arial',18))
        self.turnLabel.grid(row=9,column=1)
        # set up Jump Again label
        self.jumpLabel = Label(self,text='',font=('Arial',18))
        self.jumpLabel.grid(row=9,column=4,columnspan=4)
        # set up click status
        self.click = False
        self.old_coord = (0,0)
        self.change_player = True
        self.jump_pos = (0,0)
        self.jump_again = False
        # update
        self.update_display()

    def get_click(self, event) :
        '''CheckersGame.get_click(event)
        event handler for mouse click
        gets click data and tries to make the move'''
        coords = event.widget.get_position()
        if self.jump_again == True :
            if coords == self.jump_pos :
                square = self.squares[self.old_coord]
                square.deselect_checker()
                self.click = False
                self.board.move_checker(self.old_coord, coords)
                mid = ((self.old_coord[0] + coords[0]) // 2, (self.old_coord[1] + coords[1]) // 2)
                self.squares[mid].king = False
                if self.squares[self.old_coord].king == True :
                    self.squares[self.old_coord].king = False
                    self.squares[coords].king = True
                self.check_kings()
                self.update_display()  # update the display
                self.board.change_player()
                self.change_player = True
                self.jump_again = False
                self.jumpLabel['text'] = ""
        else :
            if self.click == False :
                self.old_coord = coords
                square = self.squares[coords]
                square.select_checker()
                self.click = True
                self.update_display()  # update the display
            elif self.squares[self.old_coord].king == True :
                if self.board.is_legal_king(self.old_coord, coords) :
                    square = self.squares[self.old_coord]
                    square.deselect_checker()
                    self.squares[self.old_coord].king = False
                    self.squares[coords].king = True
                    self.click = False
                    self.board.move_checker(self.old_coord, coords)
                    if self.board.jump == True :
                        if self.board.check_possible_jumps(coords) == True :
                            self.old_coord = coords
                            self.jump_pos = self.board.new_coords
                            self.change_player = False
                            self.jumpLabel['text'] = "Must continue jump!"
                            self.jump_again = True
                            self.click = True
                            self.squares[coords].select_checker()
                    self.squares[self.old_coord].king = False
                    self.squares[coords].king = True
                    self.update_display()  # update the display
                    if self.change_player :
                        self.board.change_player()
            elif self.board.is_legal_move(self.old_coord, coords) :
                square = self.squares[self.old_coord]
                square.deselect_checker()
                self.click = False
                self.board.move_checker(self.old_coord, coords)
                if self.board.jump == True :
                    mid = ((self.old_coord[0] + coords[0]) // 2, (self.old_coord[1] + coords[1]) // 2)
                    self.squares[mid].king = False
                    if self.board.check_possible_jumps(coords) == True :
                        self.old_coord = coords
                        self.jump_pos = self.board.new_coords
                        self.change_player = False
                        self.jumpLabel['text'] = "Must continue jump!"
                        self.jump_again = True
                        self.click = True
                        self.squares[coords].select_checker()
                self.update_display()  # update the display
                if self.change_player :
                    self.board.change_player()
            else :
                square = self.squares[self.old_coord]
                square.deselect_checker()
                self.click = False
        self.check_kings()
        self.update_display()
        if self.check_endgame() :
            message = 'Congratulations -- ' + self.colors[self.board.currentPlayer] + ' Player won!'
            messagebox.showinfo('Checkers', message, parent=self)

    def update_display(self) :
        '''CheckersGame.update_display()
        updates squares to match board
        also updates turn label square
        '''
        # update squares
        for row in range(8) :
            for column in range(8) :
                coord = (row,column)
                piece = self.board.get_piece(coord)
                if piece != -1 :
                    if self.squares[coord].king :
                        self.squares[coord].place_checker(self.colors[piece])
                        self.squares[coord].make_king()
                    else :
                        self.squares[coord].place_checker(self.colors[piece])
                else :
                    self.squares[coord].remove_checker()
        # update the turn indicator
        newPlayer = self.board.get_player()
        self.turnSquare.place_checker(self.colors[newPlayer])
        self.turnSquare.configure(highlightbackground='light gray')

    def check_kings(self) :
        row = self.board.get_row(0)
        for square in row :
            if square[1] == 1 :
                self.squares[square[0]].make_king()
                # self.board.promote_checker(square[0], 1)
        row = self.board.get_row(7)
        for square in row :
            if square[1] == 0 :
                self.squares[square[0]].make_king()
                # self.board.promote_checker(square[0], 0)

    def check_endgame(self) :
        '''CheckersGame.check_endgame()
        checks if game is over
        updates endgameMessage if over'''
        count = 0
        for row in range(8) :
            for col in range(8) :
                if self.board.get_piece((row,col)) == self.board.get_player() :
                    count += 1
        if count > 0 :
            return False
        else :
            return True


# created this tester for testing CheckersSquare
class CheckersSquareTest(Frame):
    '''a small application to test the checkers square'''

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.cell = CheckersSquare(self, 0, 0)
        self.cell.make_king()


# created this tester for testing CheckersGame
class CheckersGameTest(Frame):
    '''a small application to test the checkers game'''

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.board = CheckersGame(master)


def play_checkers() :
    # test application
    root = Tk()
    root.title("Checkers")
    # test = CheckersSquareTest(root)
    test = CheckersGameTest(root)
    root.mainloop()

play_checkers()