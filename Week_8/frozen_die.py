'''Create a subclass of our GUIDie class from this week's lesson called GUIFreezeableDie.
Objects in the subclass are dice that can be "frozen" so that they can't be rolled
until they are "unfrozen".
Specifically:

* When the die is unfrozen: its background should be white, and the roll() method
should roll the die as normal.
* When the die is frozen: its background should be gray, and the roll() method should not change
the value of the die (that is, the roll() method should do nothing).

You should:

* Add an attribute isFrozen that is True when the die is frozen, and False when the die is unfrozen
(the die should start out unfrozen).
* Add an accessor method is_frozen() that returns True if the die is frozen, False otherwise.
* Add a method toggle_freeze() that changes the die's state from frozen to unfrozen
or from unfrozen to frozen. (This method should also change the background color of
the die as described above.)
* Overload the roll() method of the subclass so that the die doesn't get rolled if it's frozen.

Here's some code to get you started. You should copy-and-paste the GUIDie class code from this week's lesson.
We've also provided a small test application to test your new subclass.
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

# test application
root = Tk()
test = FreezeTest(root)
root.mainloop()