'''Write event listeners and handlers for the following program, so that:

* When the up-arrow key is pressed, each turtle moves forward between 1 and 50 units (at random)
* When the left-arrow or right-arrow key is pressed, each turtle turns left or right --
the red turtle turns 15 degrees, the blue turtle turns 30 degrees,
and the green turtle turns 40 degrees.
'''

import turtle
import random

# you should add handlers
def up_random() :
    tRed.forward(random.randint(1,50))
    tBlue.forward(random.randint(1,50))
    tGreen.forward(random.randint(1,50))

def turn_turtle_left() :
    tRed.left(15)
    tBlue.left(30)
    tGreen.left(40)

def turn_turtle_right() :
    tRed.right(15)
    tBlue.right(30)
    tGreen.right(40)

# set up window and turtles
wn = turtle.Screen()
tRed = turtle.Turtle()
tRed.color('red')
tBlue = turtle.Turtle()
tBlue.color('blue')
tGreen = turtle.Turtle()
tGreen.color('green')

# listeners
wn.onkey(up_random, "Up")
wn.onkey(turn_turtle_left, "Left")
wn.onkey(turn_turtle_right, "Right")

# listen and run
wn.listen()
wn.mainloop()
