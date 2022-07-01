# import turtle

# # handler function for spacebar keypress event
# def spacebar_pressed():
#     print("You pressed the spacebar!")
#     wn.ontimer(after_five_seconds, 5000)

# # handler function for up-arrow keypress event
# def uparrow_pressed():
#     print("You pressed the Up arrow!")

# # handler function for mouse click event
# def mouse_clicked(x,y):
#     print("You clicked the mouse at ({:.0f},{:.0f})!".format(x,y))

# # handler function for timer event
# def after_five_seconds():
#     print("You pressed the spacebar 5 seconds ago!")

# # create a new window
# wn = turtle.Screen()

# # listener for a spacebar or Up-Arrow keypress
# wn.onkey(spacebar_pressed, "space")
# wn.onkey(uparrow_pressed, "Up")
# wn.onclick(mouse_clicked)

# # have the window listen and wait
# wn.listen()
# wn.mainloop()



# import turtle

# class SpecialTurtle(turtle.Turtle):
#     # handler methods
#     def move_forward(self):
#         self.forward(50)
#     def turn_left(self, x, y):
#         self.left(45)
#     def turn_right(self, x, y):
#         self.right(45)

# # initialize window and turtle
# wn = turtle.Screen()
# alex = SpecialTurtle()

# # listeners
# wn.onkey(alex.move_forward, "space") # spacebar press
# wn.onclick(alex.turn_left)    # left button press
# wn.onclick(alex.turn_right, 2) # right button press (2-button mouse)
# wn.onclick(alex.turn_right, 3) # right button press (3-button mouse)

# # have the window listen and wait
# wn.listen()
# wn.mainloop()


# import turtle

# class Cookie(turtle.Turtle):
#     '''represents a Chomp cookie'''

#     def __init__(self,x,y,poison):
#         '''Cookie(x,y,poison) -> Cookie
#         creates a Cookie at (x,y)
#         poison cookie if poison is True, regular otherwise'''
#         # initialize a new turtle
#         turtle.Turtle.__init__(self)
#         # make it cookie-shaped
#         self.shape('circle')
#         self.width(20)
#         # move into position
#         self.speed(0)
#         self.penup()
#         self.goto(x,y)
#         # non-poison cookies are brown
#         if not poison:
#             self.color('brown')

# class ChompGame:
#     '''represents a game of Chomp'''

#     def __init__(self,width,height):
#         '''ChompGame(width,height) -> ChompGame
#         plays a game of Chomp on a width-by-height board'''
#         # set up window
#         self.window = turtle.Screen()
#         self.window.title('Chomp')
#         # set up game data
#         self.gamewidth = width
#         self.gameheight = height
#         self.cookies = {}  # store the cookies
#         for i in range(width):
#             for j in range(height):
#                 self.cookies[(i,j)] = Cookie(40*i,40*j,i==0 and j==0)
#         # set up turtle to write game messages
#         self.messenger = turtle.Turtle()
#         self.messenger.hideturtle()
#         self.messenger.penup()
#         self.messenger.goto(0,-100)
#         # set up player
#         self.player = 1
#         self.print_player()
#         # start the game
#         self.window.onclick(self.chomp)  # listen for clicks
#         self.window.listen()
#         self.window.mainloop()

#     def print_player(self):
#         '''ChompGame.print_player()
#         print the current player's turn information'''
#         self.messenger.clear()
#         self.messenger.write("Player "+str(self.player)+"'s turn",
#                              font=("Arial",36,"normal"))

#     def chomp(self,x,y):
#         '''ChompGame.chomp(x,y)
#         listener for mouse clicks'''
#         # get the cookie that was just clicked on
#         x = round(x/40)
#         y = round(y/40)
#         # make sure it's a valid click
#         if (0 <= x < self.gamewidth) and (0 <= y < self.gameheight) \
#            and self.cookies[(x,y)].isvisible():
#             # remove all cookies above and/or to the right
#             for i in range(x,self.gamewidth):
#                 for j in range(y,self.gameheight):
#                     self.cookies[(i,j)].hideturtle()
#             # check for the poison cookie
#             if x+y == 0:
#                 print("Player "+str(self.player)+" loses!")
#                 self.window.bye()
#                 return
#             # go to the other player
#             self.player = 3 - self.player
#             self.print_player()

# ChompGame(5,7)

# from tkinter import *

# class HelloWorldFrame(Frame):
#     '''creates a hello world window'''

#     def __init__(self,master):
#         '''HelloWorldFrame()
#         creates a new HelloWorldFrame'''
#         Frame.__init__(self,master)  # set up as a Tk frame
#         self.grid()  # place the frame in the root window
#         # create a button
#         self.hwButton = Button(self,text='Click me!',command=self.print_message)
#         self.hwButton.grid(row=0,column=0)
#         # create a text display
#         self.hwMessageBox = Label(self,text="I'm waiting...")
#         self.hwMessageBox.grid(row=1,column=0)

#     def print_message(self):
#         '''prints hello world message'''
#         self.hwMessageBox['text'] = 'Hello, World!'

# root = Tk()
# hwf = HelloWorldFrame(root)
# hwf.mainloop()

from tkinter import *
import random

class TwoNumbersFrame(Frame):
    '''a frame for our two-numbers app'''

    def __init__(self,master):
        '''TwoNumbersFrame(master)'''
        Frame.__init__(self,master)
        self.grid()
        master.title('Two numbers')
        # generate two random numbers and display them
        self.label0 = Label(self)
        self.label0.grid(row=0,column=0)
        self.label1 = Label(self)
        self.label1.grid(row=0,column=1)
        self.new_numbers()
        # generate smaller and bigger buttons
        Button(self,text='Smaller',command=self.smaller).grid(row=1,column=0)
        Button(self,text='Larger',command=self.larger).grid(row=1,column=1)
        # generate new number buttons
        Button(self,text='New Numbers',command=self.new_numbers).grid(columnspan=2)

    def new_numbers(self):
        '''TwoNumbersFrame.new_numbers()
        generates new numbers and updates the display'''
        self.num0 = random.randrange(100)
        self.num1 = random.randrange(100)
        self.label0['text'] = str(self.num0)
        self.label0['background'] = 'white'
        self.label1['text'] = str(self.num1)
        self.label1['background'] = 'white'

    def smaller(self):
        '''TwoNumbersFrame.smaller()
        highlights the smaller number'''
        if self.num0 > self.num1:
            self.label0['background'] = 'white'
            self.label1['background'] = 'lightblue'
        elif self.num0 < self.num1:
            self.label0['background'] = 'lightblue'
            self.label1['background'] = 'white'

    def larger(self):
        '''TwoNumbersFrame.larger()
        highlights the larger number'''
        if self.num0 > self.num1:
            self.label0['background'] = 'lightblue'
            self.label1['background'] = 'white'
        elif self.num0 < self.num1:
            self.label0['background'] = 'white'
            self.label1['background'] = 'lightblue'

# create new window and initialize and run the frame
root = Tk()
tnf = TwoNumbersFrame(root)
tnf.mainloop()