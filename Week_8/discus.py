'''Use the GUIFreezeableDie class from part (a) to write the game Discus
(yet another of Reiner Knizia's Decathlon games).

Rules:

Player gets 3 attempts -- the highest score from the 3 attempts is the player's final score.
Each attempt uses 5 dice. Only the even sides (2,4,6) count towards a player's score --
the odd sides (1,3,5) count for 0.

To start an attempt, the player rolls all 5 dice. The player must freeze one or more of the scoring dice
(only even-valued dice can be frozen) -- if the player cannot freeze any dice, the attempt is fouled
and scores 0. Once frozen, a die cannot be unfrozen.

The player can then stop and score the sum of the even dice, or may reroll the unfrozen dice.
The player must freeze at least one new die after each reroll -- if the player cannot do so
(because all the rerolled dice landed on odd numbers), then the attempt is fouled with a score of 0.
The player can stop at any time and score the sum of the even dice.

A screenshot of a sample play of the game is shown below. Note that at times
the player tried to reroll without freezing a die, and the game did not permit this.
Also note the "Freeze" buttons get activated or disabled, as appropriate, after each roll.
The final attempt was fouled because an odd number was rolled on the final reroll.
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


class GUIFreezeableDie(GUIDie):
    '''a GUIDie that can be "frozen" so that it can't be rolled'''

    def __init__(self,master,valueList=[1,2,3,4,5,6],colorList=['black']*6):
        '''GUIFreezeableDie(master,[valueList,colorList]) -> GUIFreezeableDie
        creates a GUI 6-sided freeze-able die
          valueList is the list of values (1,2,3,4,5,6 by default)
          colorList is the list of colors (all black by default)'''
        # create a 60x60 white canvas with a 5-pixel grooved border
        Canvas.__init__(self,master,width=60,height=60,bg='white',\
                        bd=5,relief=GROOVE)
        self.freezeButton = Button(self,text='Freeze',command=self.toggle_freeze)
        self.freezeButton.grid(row=2,columnspan=1)
        # store the valuelist and colorlist
        self.valueList = valueList
        self.colorList = colorList
        # initialize the top value
        self.top = 1
        # initializes the frozen state
        self.frozen = False

    def is_frozen(self):
        '''GUIFreezeableDie.is_frozen() -> bool
        returns True if the die is frozen, False otherwise'''
        return self.frozen
    
    def toggle_freeze(self):
        '''GUIFreezeableDie.toggle_freeze()
        toggles the frozen status'''
        self.frozen = not self.frozen

    def roll(self):
        '''GuiFreezeableDie.roll()
        overloads GUIDie.roll() to not allow a roll if frozen'''
        if not self.frozen :
            self.top = random.randrange(1,7)
            self.draw()


class FreezeTest(Frame):
    '''a small application to test the freezeable die'''

    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.die = GUIFreezeableDie(self)
        self.die.grid()
        Button(self,text='Roll',command=self.die.roll).grid()
        Button(self,text='Toggle Freeze',command=self.die.toggle_freeze).grid()


class DiscusFrame(Frame):
    '''frame for a game of discus'''

    def __init__(self,master,name):
        '''DiscusFrame(master,name) -> DiscusFrame
        creates a new discus frame
        name is the name of the player'''
        # set up Frame object
        Frame.__init__(self,master)
        self.grid()
        # label for player's name
        Label(self,text=name,font=('Arial',18)).grid(columnspan=3,sticky=W)
        # set up score and rerolls
        self.scoreLabel = Label(self,text='Attempt # 1  Score: 0',font=('Arial',18))
        self.scoreLabel.grid(row=0,column=2,columnspan=2)
        self.rerollLabel = Label(self,text='High Score: 0',font=('Arial',18))
        self.rerollLabel.grid(row=0,column=5,columnspan=3,sticky=E)
        # set up directions
        self.directionLabel = Label(self,text='Click Roll button to start',font=('Arial',18))
        self.scoreLabel.grid(row=2,column=2,columnspan=2)
        # initialize game data
        self.score = 0
        self.rerolls = 5
        self.gameround = 0
        self.high_score = 0
        # set up dice
        self.dice = []
        for n in range(5):
            self.dice.append(GUIDie(self,[1,2,3,4,5,-6],['black']*5+['red']))
            self.dice[n].grid(row=1,column=n)
        # set up buttons
        self.rollButton = Button(self,text='Roll',command=self.roll)
        self.rollButton.grid(row=1,column=6,columnspan=1)
        self.keepButton = Button(self,text='Keep',state=DISABLED,command=self.keep)
        self.keepButton.grid(row=2,column=6,columnspan=1)

    def roll(self):
        '''Decath100MFrame.roll()
        handler method for the roll button click'''
        # roll both dice
        self.dice[4*self.gameround].roll()
        self.dice[4*self.gameround+1].roll()
        self.dice[4*self.gameround+2].roll()
        self.dice[4*self.gameround+3].roll()
        # if this was the first roll of the round, turn on the keep button
        if self.keepButton['state'] == DISABLED :
            self.keepButton['state'] = ACTIVE
        else:  # otherwise we just spent a reroll
            self.rerolls -= 1
            self.rerollLabel['text'] = 'Rerolls: '+str(self.rerolls)
        if (self.rerolls == 0):  # no rerolls left, so turn off roll button
            self.rollButton['state'] = DISABLED

    def keep(self):
        '''Decath100MFrame.keep()
        handler method for the keep button click'''
        # add dice to score and update the scoreboard
        self.score += self.dice[4*self.gameround].get_top() + \
                      self.dice[4*self.gameround+1].get_top() + \
                      self.dice[4*self.gameround+2].get_top() + \
                      self.dice[4*self.gameround+3].get_top()
        self.scoreLabel['text'] = 'Score: '+str(self.score)
        self.gameround += 1  # go to next round
        if self.gameround < 2:  # move buttons to next pair of dice
            self.rollButton.grid(row=2,column=4*self.gameround,columnspan=4)
            self.keepButton.grid(row=3,column=4*self.gameround,columnspan=4)
            self.rollButton['state'] = ACTIVE
            self.keepButton['state'] = DISABLED
        else:  # game over
            self.keepButton.grid_remove()
            self.rollButton.grid_remove()
            self.rerollLabel['text'] = 'Game over'

# play the game with multiple players
numPlayers = int(input("How many players? "))
playerList = []
for n in range(numPlayers):
    playerList.append(input("Player "+str(n+1)+", enter your name: "))
root = Tk()
root.title('100 Meters')
for n in range(numPlayers):
    DiscusFrame(root,playerList[n])
root.mainloop()