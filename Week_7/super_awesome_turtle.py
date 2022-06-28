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
        self.speed = 0
        # the getscreen() method returns the Screen object that
        #    the turtle lives in
        self.getscreen().onkey(self.stop,'s')
        self.getscreen().onkey(self.quit,'q')
        self.getscreen().onkey(self.go_forward,'Up')
        self.getscreen().onkey(self.go_backward,'Down')
        self.getscreen().onkey(self.left(90),'Left')
        self.getscreen().onkey(self.right(90),'Right')
        self.go()

    def go(self) :
        if self.move :
            self.forward(self.speed)

    def go_forward(self):
        self.move = True
        self.speed += 25
        self.go()
        # self.forward(1)
        # self.getscreen().ontimer(self.goforward,25)
            
    def go_backward(self):
        self.move = True
        self.speed -= 25
        self.go()
        # self.forward(1)
        # self.getscreen().ontimer(self.goforward,-25)

    def stop(self):
        self.move = False

    def quit(self) :
        self.getscreen().bye()

wn = turtle.Screen()
pete = SuperAwesomeTurtle()
wn.listen()
wn.mainloop()