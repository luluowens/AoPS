'''Specifically, write a function play_minesweeper(width,height,numBombs) that launches a
tkinter window to play the game Minesweeper on a $width \times height$ board of squares,
with numBombs of the squares randomly selected to contain bombs.

The goal in Minesweeper is to expose all the squares that do not contain bombs.
The player exposes a square by left-clicking on it.

-- If the square contains a bomb, KABOOM! -- the game is over and the player loses.
The game should display all of the remaining unexposed, unflagged bombs. (See below about "flagging".)

-- If the square does not contain a bomb, it displays a number that indicates the number of
adjacent squares (including diagonally-adjacent) that contain a bomb.
(If none of the adjacent squares contain a bomb, the exposed square is blank --
you can optionally have the game auto-expose all of the adjacent squares, because
since you know that none of them are bombs, it's safe to do so.) If the player successfully exposes
all the non-bomb squares, the player wins.

The player may also flag squares that he/she believes to contain a bomb, by right-clicking on them.
Flagged squares should display as asterisks, and cannot be exposed unless they are unflagged by
again right-clicking on them (which also removes the asterisk).
The game should also display the number of bombs minus the number of placed flags.
'''

from tkinter import *

class MineCell(Canvas) :
    '''1 cell of a Minesweeper game'''

    def __init__(self,master,adjacent,mine,colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']):
        '''MineCell(master,[adjacent,colorList]) -> MineCell
        creates a GUI Minesweeper Cell
          adjacent is the list of adjacent cells
          colormap is the list of colors for different number values
        '''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=25,height=25,bg='white',\
                        bd=2,relief=RAISED)
        # store the value and color of the number
        self.value = 0
        self.mine = mine
        self.flagged = False
        for i in adjacent :
            if i.mine :
                self.value += 1
        self.color = colormap[self.value]
        # bind a button with right-clicks to the cell
        self.bind('<Button-1>', self.press)
        # bind a button with right-clicks to the cell
        self.bind('<Button-2>', self.flag)

    def press(self, event):
        '''MineCell.press()
        displays the number of adjacent bombs in the cell
        '''
        # check if there is a mine
        if self.mine :
            self.explode()
        else :
            # press cell in
            self.configure(bg='light gray')  # sets background color to gray
            self.configure(relief=SUNKEN)  # puts cell "inside" the screen
            if self.value != 0 :
                self.create_text(17, 17, text=str(self.value), fill=self.color, font=('Arial 20'))

    def flag(self, event):
        '''Minecell.flag()
        flags the cell
        '''
        # puts an asterisk on cell, does not change bg color
        self.create_text(17, 17, text="*", fill='black', font=('Arial 20'))
        self.flagged = True

    def explode(self):
        '''Minecell.explode()
        explodes the bomb under that cell
        '''
        # sets background color to red and draw "bomb"
        self.configure(bg='red')
        self.create_text(17, 17, text="*", fill='black', font=('Arial 20'))
        


class MineCellTest(Frame):
    '''a small application to test the minesweeper cell'''

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        # self.cell_1 = MineCell(self, [], False)
        self.cell_1 = MineCell(self, [], True)
        self.cell_1.grid()
        # Button(self,text='Roll',command=self.die.roll).grid()
        # Button(self,text='Toggle Freeze',command=self.die.toggle_freeze).grid()


# test application
root = Tk()
root.title("Minesweeper")
test = MineCellTest(root)
root.mainloop()
