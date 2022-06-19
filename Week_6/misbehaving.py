'''Some turtles (not too many, fortunately) like to misbehave.
If you ask them to turn left, 25% of the time they'll turn right instead,
and if you ask them to turn right, 25% of the time they'll turn left instead.

Create a new subclass MisbehavingTurtle to implement this naughty behavior.
Then run the test code below and see how our new turtles act.
'''

import turtle
import random

class MisbehavingTurtle(turtle.Turtle):
    #You fill in the rest.
    def __init__(self) :
        turtle.Turtle.__init__(self)

    def right(self, angle) :
        turn_other = random.randint(1,4)
        if turn_other == 1 :
            turtle.Turtle.left(self, angle)
        else :
            turtle.Turtle.right(self, angle)

    def left(self, angle) :
        turn_other = random.randint(1,4)
        if turn_other == 1 :
            turtle.Turtle.right(self, angle)
        else :
            turtle.Turtle.left(self, angle)

# test case
# drawing an octagon and a square
def drawing_test(t):
    '''drawing_test(t)
     draws an octagon and square with t'''
    for i in range(8):
        t.forward(30)
        t.left(45)
    t.right(45)
    for i in range(4):
        t.forward(50)
        t.right(90)
        
# one nice turtle and one not-so-nice turtle
wn = turtle.Screen()
sugar = turtle.Turtle()
sugar.color('green')
drawing_test(sugar)
spice = MisbehavingTurtle()
spice.color('red')
drawing_test(spice)
wn.mainloop()