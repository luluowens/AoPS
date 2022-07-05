'''Use our GUIDie class to write the game Shot Put (another one of Reiner Knizia's Decathlon games).

Rules: Player gets 3 attempts--the highest score from the 3 attempts is the player's final score.
On each attempt: player rolls one die at a time and adds to the attempt score.
Rolling a 1 is a foul and ends the attempt with a score of 0.
At any time the player can stop--the total of the dice thrown on the attempt is the player's score for
that attempt. The player must stop if they have rolled 8 dice during an attempt without a foul.

A screen capture of a sample play of the game is shown below. Note that Attempt 1 ended in a foul.
'''

from tkinter import *
import random

class GUIDie(Canvas):
    '''6-sided Die class for GUI'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIDie(master,[valueList,colorList]) -> GUIDie
        creates a GUI 6-sided die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1

    def get_top(self):
        '''GUIDie.get_top() -> int
        returns the value on the die'''
        return self.valueList[self.top-1]

    def roll(self):
        '''GUIDie.roll()
        rolls the die'''
        self.top = random.randrange(1,7)
        self.draw()

    def draw(self):
        '''GUIDie.draw()
        draws the pips on the die'''
        # clear old pips first
        self.erase()
        # location of which pips should be drawn
        pipList = [[(1,1)],
                   [(0,0),(2,2)],
                   [(0,0),(1,1),(2,2)],
                   [(0,0),(0,2),(2,0),(2,2)],
                   [(0,0),(0,2),(1,1),(2,0),(2,2)],
                   [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)]]
        for location in pipList[self.top-1]:
            self.draw_pip(location,self.colorList[self.top-1])

    def draw_pip(self,location,color):
        '''GUIDie.draw_pip(location,color)
        draws a pip at (row,col) given by location, with given color'''
        (centerx,centery) = (17+20*location[1],17+20*location[0])  # center
        self.create_oval(centerx-5,centery-5,centerx+5,centery+5,fill=color)

    def erase(self):
        '''GUIDie.erase()
        erases all the pips'''
        pipList = self.find_all()
        for pip in pipList:
            self.delete(pip)



class shot_put_frame(Frame):
    '''frame for a game of Shot Put'''

    def __init__(self,master,name):
        '''shot_put_frame(master,name) -> shot_put_frame
        creates a new Shot Put frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # set up score and rerolls
        self.scoreLabel = Label(self,text='Attempt #1  Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=3,columnspan=2)
        self.highLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.highLabel.grid(row=0,column=5,columnspan=3,sticky=E)
        # initialize game data
        self.score = 0
        self.high_score = 0
        self.attempt = 1
        self.gameround = 0
        # set up dice
        self.dice = []
        for n in range(8):
            self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=2,columnspan=1)
        self.stopButton = Button(self,text='Stop',state=DISABLED,command=self.stop)
        self.stopButton.grid(row=3,columnspan=1)

    def roll(self):
        '''shot_put_frame.roll()
        handler method for the roll button click'''
        # roll die
        self.dice[self.gameround].roll()
        # add dice to score and update the scoreboard
        self.score += self.dice[self.gameround].get_top()
        self.scoreLabel['text'] = F'Attempt #{self.attempt} Score: {self.score}'
        # check if foul has occurred
        if self.dice[self.gameround].get_top() == 1 :
            self.rollButton['state'] = DISABLED
            self.stopButton['text'] = "FOUL"
            self.stopButton['state'] = ACTIVE
            self.scoreLabel['text'] = "FOULED ATTEMPT"
            self.score = 0
        else :
            self.gameround += 1
            if self.gameround < 8:  # move buttons to next pair of dice
                self.rollButton.grid(row=2,column=self.gameround,columnspan=1)
                self.stopButton.grid(row=3,column=self.gameround,columnspan=1)
                self.rollButton['state'] = ACTIVE
                self.stopButton['state'] = ACTIVE
            else :
                self.rollButton['state'] = DISABLED
                self.stopButton['state'] = ACTIVE

    def stop(self):
        '''shot_put_frame.stop()
        handler method for the stop button click'''
        self.gameround = 0 # go to next round
        # we are done with this attempt
        self.attempt += 1
        self.scoreLabel['text'] = f'Attempt #{self.attempt}  Score: 0'
        if self.high_score <= self.score :
            self.high_score = self.score
        self.highLabel['text'] = f'High Score: {self.high_score}'
        # game is over
        if self.attempt > 3 :
            self.stopButton.grid_remove()
            self.rollButton.grid_remove()
            self.scoreLabel['text'] = 'Game over'
        else :
            # set up dice
            self.dice = []
            for n in range(8):
                self.dice.append(GUIDie(self,[1,2,3,4,5,6],['red']+['black']*5))
                self.dice[n].grid(row=1,column=n)
            # set up buttons
            self.rollButton.grid(row=2,column=self.gameround,columnspan=1)
            self.stopButton.grid(row=3,column=self.gameround,columnspan=1)
            self.rollButton['state'] = ACTIVE
            self.stopButton['text'] = "Stop"
            self.stopButton['state'] = DISABLED


name = (input("Please enter your name: "))
root = Tk()
root.title('Shot Put')
shot_put_frame(root, name)
root.mainloop()