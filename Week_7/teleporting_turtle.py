'''Complete the following code to create a teleporting turtle:
when the user clicks on a location, the turtle instantly moves to that location.
A left click draws the line from the previous position to the new position,
and a right click moves the turtle without drawing a line.

Note: Your right mouse button may be button 2 or button 3.
'''

import turtle

def teleport_and_draw(x, y) :
    carol.pendown()
    carol.goto(x,y)

def teleport_and_no_draw(x, y) :
    carol.penup()
    carol.goto(x,y)

# set up window and TT
wn = turtle.Screen()
carol = turtle.Turtle()

# listeners to teleport
wn.onclick(teleport_and_draw,1)    # left click
wn.onclick(teleport_and_no_draw,2) # right click

# turn on the listeners and run
wn.listen()
wn.mainloop()