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
from tkinter import messagebox
import random

class MineCell(Canvas) :
    '''1 cell of a Minesweeper game'''

    def __init__(self,master):
        '''MineCell(master,[adjacent,colorList]) -> MineCell
        creates a GUI Minesweeper Cell
          colormap is the list of colors for different number values
        '''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=25,height=25,bg='white',\
                        bd=2,relief=RAISED)
        # store the value and color of the number
        self.colormap = ['','blue','darkgreen','red','purple','maroon','cyan','black','dim gray']
        self.value = 0
        self.mine = False
        self.flagged = False
        self.exploded = False
        self.pressed = False
        self.flag_count = 0
        # bind a button with left-clicks to the cell
        self.bind('<Button-1>', self.press)
        # bind a button with center-clicks (right-clicks trackpad users) to the cell
        self.bind('<Button-2>', self.flag)
        # bind a button with right-clicks to the cell
        self.bind('<Button-3>', self.flag)

    def get_mine_status(self) :
        '''returns boolean for if there is a mine under this cell
        '''
        return self.mine

    def place_mine(self) :
        '''puts a mine under this cell
        '''
        self.mine = True

    def set_value(self, value) :
        '''set the number of adjacent mines
        '''
        self.value = value
    
    def get_value(self) :
        '''returns number of adjacent mines
        '''
        return self.value

    def press(self, event):
        '''MineCell.press()
        displays the number of adjacent bombs in the cell
        '''
        # check if there is a mine
        if self.mine :
            self.explode()
            self.exploded = True
        else :
            # press cell in
            self.configure(bg='light gray')  # sets background color to gray
            self.configure(relief=SUNKEN)  # puts cell "inside" the screen
            color = self.colormap[self.value]
            if self.value != 0 :
                self.create_text(17, 17, text=str(self.value), fill=color, font=('Arial 20'))
            self.pressed = True # sets the cell to being pressed
        # increment total number of pressed cells
        self.master.add_pressed_cells()
        # check if game is over
        self.master.game_over()

    def flag(self, event):
        '''Minecell.flag()
        flags the cell
        '''
        # check if this right (or central) click is deflagging cell
        if self.flag_count % 2 == 1 :
            # deflag the cell
            self.delete(self.flag)
            self.flagged = False
            # decrease total number of pressed cells
            self.master.subtract_pressed_cells()
            # decrease frame mine number
            self.master.increase_mine_number()
        else :
            # puts an asterisk on cell, does not change bg color
            self.flag = self.create_text(17, 17, text="*", fill='black', font=('Arial 20'))
            self.flagged = True
            # increment total number of pressed cells
            self.master.add_pressed_cells()
            # increase frame mine number
            self.master.decrease_mine_number()
            # check if game is over
            self.master.game_over()
        self.flag_count += 1
        

    def explode(self):
        '''Minecell.explode()
        explodes the bomb under that cell
        '''
        # sets background color to red and draw "bomb"
        self.configure(bg='red')
        self.create_text(17, 17, text="*", fill='black', font=('Arial 20'))
        # presents a "you lost" message
        messagebox.showerror('Minesweeper','KABOOM! You lose.',parent=self)
        self.master.show_mines()



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
        self.mineLabel.grid(row=rows+1,column=cols//2,columnspan=2)
        self.cols = cols
        self.rows = rows
        self.num_mines = num_mines
        self.total_pressed = 0
        # set up cells
        self.cells = []
        self.set_up_cells()


    def set_up_cells(self) :
        '''creating individual cells in self.cells
        setting up the mines
        '''
        # create the cols x rows cells
        for i in range(self.rows):
            row = []
            for j in range(self.cols) :
                row.append(MineCell(self))
            self.cells.append(row)

        # display cells
        for i in range(self.rows) :
            for j in range(self.cols) :
                self.cells[i][j].grid(row=i+1,column=j+1)
        
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
        '''adjust Cell.adjacent for adjacent mines
        '''
        for i in range(self.rows) :
            for j in range(self.cols) :
                if self.cells[i][j].get_value() == 0 :
                    adjacent = 0
                    adj_cells = []
                    # check if cell as adjacencies to its left
                    if i > 0 :
                        adj_cells.append(self.cells[i-1][j])
                        if j > 0 :   # check if cell as adjacencies above
                            adj_cells.append(self.cells[i-1][j-1])
                        if j < self.cols - 1 :   # check if cell as adjacencies below
                            adj_cells.append(self.cells[i-1][j+1])
                    # check if cell has adjacencies to its right
                    if i < self.rows - 1 :
                        adj_cells.append(self.cells[i+1][j])
                        if j > 0 :   # check if cell as adjacencies above
                            adj_cells.append(self.cells[i+1][j-1])
                        if j < self.cols - 1:   # check if cell as adjacencies below
                            adj_cells.append(self.cells[i+1][j+1])
                    # while keeping the row the same...
                    if j > 0 :   # check if cell as adjacencies above
                        adj_cells.append(self.cells[i][j-1])
                    if j < self.cols - 1 :   # check if cell as adjacencies below
                        adj_cells.append(self.cells[i][j+1])
                    # check if adjacent cells have mines
                    for cell in adj_cells :
                        if cell.get_mine_status() :
                            adjacent += 1
                    # set adjacency number
                    self.cells[i][j].set_value(adjacent)
        

    def update_mine_number(self) :
        self.mineLabel['text'] = str(self.num_mines)

    def decrease_mine_number(self) :
        '''decreases the number of mines left by 1
        '''
        self.num_mines -= 1
        self.update_mine_number()

    def increase_mine_number(self) :
        '''increases the number of mines left by 1
        this only happens when player unflags a cell
        '''
        self.num_mines += 1
        self.update_mine_number()

    def add_pressed_cells(self) :
        '''increments the total number of displayed or flagged cells by 1
        '''
        self.total_pressed += 1

    def subtract_pressed_cells(self) :
        '''decreases the total number of displayed or flagged cells by 1
        this only happens when player unflags a cell
        '''
        self.total_pressed -= 1

    def game_over(self) :
        '''check if player has won by "pressing" all cells
        '''
        if self.total_pressed == self.rows * self.cols :
            messagebox.showinfo('Minesweeper','Congratulations -- you won!',parent=self)


    def show_mines(self) :
        '''displays all mined cells after player presses a cell with a mine
        '''
        for row in self.cells :
            for cell in row :
                if cell.mine :
                    cell.configure(bg='red')
                    cell.create_text(17, 17, text="*", fill='black', font=('Arial 20'))



def  play_minesweeper(width,height,numBombs) :
    '''main function that sets up a new MinesweeperFrame
    '''
    MinesweeperFrame(root, width, height, numBombs)


# # created this tester for testing MineCell
# class MineCellTest(Frame):
#     '''a small application to test the minesweeper cell'''

#     def __init__(self,master):
#         Frame.__init__(self,master)
#         self.grid()
#         self.cell_1 = MineCell(self)
#         self.cell_1.value = 2
#         # self.cell_1 = MineCell(self, [], True)
#         self.cell_1.grid()


# test application
root = Tk()
root.title("Minesweeper")
# test = MineCellTest(root)
play_minesweeper(12, 10, 15)
# play_minesweeper(3, 3, 1)
root.mainloop()
