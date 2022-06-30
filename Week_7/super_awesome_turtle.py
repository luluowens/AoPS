'''Create a SuperAwesomeTurtle that responds to the following events:

* Pressing the up-arrow key increases the turtle's speed by 25 units/second.
(So, for example, pressing "Up" three times will make the turtle go forward at a speed of 75 units/second.)
* Pressing the down-arrow key decreases the turtle's speed by 25 units/second.
(Negative speeds should make the turtle go backwards.)
* Pressing the left-arrow or right-arrow key turns the turtle 90 degrees left or right.
* Pressing the 's' key makes the turtle come to a full stop.
* Pressing the 'q' key closes the window and ends the program.
'''

import turtle

class SuperAwesomeTurtle(turtle.Turtle):
    '''a super awesome turtle!'''

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.move = True
        # sets the turtle at 25 units per sec (1 unit per 40 milisecs)
        self.speed = 40
        # the getscreen() method returns the Screen object that
        #    the turtle lives in
        self.getscreen().onkey(self.stop,'s')
        self.getscreen().onkey(self.quit,'q')
        self.getscreen().onkey(self.go_forward,'Up')
        self.getscreen().onkey(self.go_backward,'Down')
        self.getscreen().onkey(self.turn_left,'Left')
        self.getscreen().onkey(self.turn_right,'Right')
        # starts the turtle's movement
        self.go()

    def go(self) :
        # if the turtle is allowed to move, then move
        if self.move :
            if self.speed < 0 :
                self.forward(-1)
                self.getscreen().ontimer(self.go, self.speed)
            else :
                self.forward(1)
                self.getscreen().ontimer(self.go, self.speed)

    def go_forward(self):
        self.move = True
        # decrease time by 40 milisecs
        self.speed -= 40
        self.go()
            
    def go_backward(self):
        self.move = True
        # increase time by 40 milisecs
        self.speed += 40
        self.go()

    def turn_left(self) :
        # turn to the left by 90
        self.left(90)
    
    def turn_right(self) :
        # turn to the right by 90
        self.right(90)

    def stop(self):
        # sets self.move to false so self.go will not work
        self.move = False

    def quit(self) :
        # quits the screen
        self.getscreen().bye()

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()