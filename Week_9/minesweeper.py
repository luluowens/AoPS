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
import random

class MineCell(Canvas) :
    '''1 cell of a Minesweeper game'''

    def __init__(self,master,colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']):
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
        self.mine = False
        self.flagged = False
        self.adjacent = []
        for i in self.adjacent :
            if i.mine :
                self.value += 1
        self.color = colormap[self.value]
        # bind a button with right-clicks to the cell
        self.bind('<Button-1>', self.press)
        # bind a button with right-clicks to the cell
        self.bind('<Button-2>', self.flag)

    def get_mine_status(self) :
        return self.mine

    def place_mine(self) :
        self.mine = True

    def set_adjacent(self, value) :
        self.adjacent = value
    
    def get_adjacent(self) :
        return self.adjacent

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


# class MineCellTest(Frame):
#     '''a small application to test the minesweeper cell'''

#     def __init__(self,master):
#         Frame.__init__(self,master)
#         self.grid()
#         # self.cell_1 = MineCell(self, [], False)
#         self.cell_1 = MineCell(self, [], True)
#         self.cell_1.grid()


class MinesweeperFrame(Frame) :
    '''frame for a game of Minesweeper'''

    def __init__(self,master,cols,rows,num_mines):
        '''MinesweeperFrame(master) -> MinesweeperFrame
        creates a new Minesweeper frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for mines left
        self.mineLabel = Label(self,text=str(num_mines),font=('Arial',18))
        self.mineLabel.grid(row=rows+1,columnspan=1,sticky=E)
        self.cols = cols
        self.rows = rows
        self.num_mines = num_mines
        # set up cells
        self.cells = []
        self.set_up_cells()


    def set_up_cells(self) :
        # create the cols x rows cells
        for i in range(self.cols):
            for j in range(self.rows) :
                self.cells[j].append(self)
                self.cells[j][i].grid(row=j+1,column=i+1)
        
        # set up the mines
        i = 0
        while i < self.num_mines :
            random_row = random.randint(0,self.rows-1)
            random_col = random.randint(0,self.cols-1)
            cell = self.cells[random_row][random_col]
            if cell.get_mine_status() == False :
                cell.place_mine()
                i += 1
        self.set_up_adjacent()
    

    def set_up_adjacent(self) :
        # adjust numbers for adjacent mines
        # case 1: cells with 8 adjacent
        for i in range(1, self.rows) :
            for j in range(1, self.cols) :
                if self.cells[i][j].get_adjacent() == 0 :
                    adjacent = 0
                    if self.cells[i-1][j-1].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i][j-1].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i+1][j-1].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i-1][j].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i][j].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i+1][j].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i-1][j+1].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i][j+1].get_mine_status() :
                        adjacent += 1
                    elif self.cells[i+1][j+1].get_mine_status() :
                        adjacent += 1
                    self.cells[i][j].set_adjacent(adjacent)
        
        # adjust numbers for adjacent mines
        # case 2: cells with 3 adjacent on top
        for j in range(1, self.cols) :
            if self.cells[0][j].get_adjacent() == 0 :
                adjacent = 0
                if self.cells[0][j-1].get_mine_status() :
                    adjacent += 1
                elif self.cells[0][j+1].get_mine_status() :
                    adjacent += 1
                elif self.cells[1][j].get_mine_status() :
                    adjacent += 1
                self.cells[0][j].set_adjacent(adjacent)
        
        # adjust numbers for adjacent mines
        # case 3: cells with 3 adjacent on bottom
        for j in range(1, self.cols) :
            if self.cells[self.cols-1][j].get_adjacent() == 0 :
                adjacent = 0
                if self.cells[self.cols-1][j-1].get_mine_status() :
                    adjacent += 1
                elif self.cells[self.cols-1][j+1].get_mine_status() :
                    adjacent += 1
                elif self.cells[self.cols-2][j].get_mine_status() :
                    adjacent += 1
                self.cells[self.cols-1][j].set_adjacent(adjacent)

        # adjust numbers for adjacent mines
        # case 4: cells with 3 adjacent on left
        for i in range(1, self.rows) :
            if self.cells[i][0].get_adjacent() == 0 :
                adjacent = 0
                if self.cells[i-1][0].get_mine_status() :
                    adjacent += 1
                elif self.cells[i+1][0].get_mine_status() :
                    adjacent += 1
                elif self.cells[i][0].get_mine_status() :
                    adjacent += 1
                self.cells[i][0].set_adjacent(adjacent)

        # adjust numbers for adjacent mines
        # case 5: cells with 3 adjacent on right
        for i in range(1, self.rows) :
            if self.cells[i][self.rows-1].get_adjacent() == 0 :
                adjacent = 0
                if self.cells[i-1][self.rows-1].get_mine_status() :
                    adjacent += 1
                elif self.cells[i+1][self.rows-1].get_mine_status() :
                    adjacent += 1
                elif self.cells[i][self.rows-2].get_mine_status() :
                    adjacent += 1
                self.cells[i][self.rows-1].set_adjacent(adjacent)
        
        # adjust numbers for adjacent mines
        # case 6: cells with 2 adjacent, top left
        if self.cells[0][0].get_adjacent() == 0 :
            adjacent = 0
            if self.cells[1][0].get_mine_status() :
                adjacent += 1
            elif self.cells[0][1].get_mine_status() :
                adjacent += 1
            self.cells[0][0].set_adjacent(adjacent)
        
        # adjust numbers for adjacent mines
        # case 7: cells with 2 adjacent, top right
        if self.cells[0][self.cols-1].get_adjacent() == 0 :
            adjacent = 0
            if self.cells[1][self.cols-1].get_mine_status() :
                adjacent += 1
            elif self.cells[0][self.cols-2].get_mine_status() :
                adjacent += 1
            self.cells[0][self.cols-1].set_adjacent(adjacent)
        
        # adjust numbers for adjacent mines
        # case 8: cells with 2 adjacent, bottom left
        if self.cells[self.rows-1][0].get_adjacent() == 0 :
            adjacent = 0
            if self.cells[self.rows-1][1].get_mine_status() :
                adjacent += 1
            elif self.cells[self.rows-2][0].get_mine_status() :
                adjacent += 1
            self.cells[self.rows-1][0].set_adjacent(adjacent)
        
        # adjust numbers for adjacent mines
        # case 9: cells with 2 adjacent, bottom right
        if self.cells[self.rows-1][self.cols-1].get_adjacent() == 0 :
            adjacent = 0
            if self.cells[self.rows-1][self.cols-2].get_mine_status() :
                adjacent += 1
            elif self.cells[self.rows-2][self.cols-1].get_mine_status() :
                adjacent += 1
            self.cells[self.rows-1][self.cols-1].set_adjacent(adjacent)


    # def make_move(self) :


# test application
root = Tk()
root.title("Minesweeper")
# test = MineCellTest(root)
root.mainloop()
