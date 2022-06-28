'''Write a tkinter-based program that opens a window with a button and the label.
The label should keep track of how many times the button has been clicked.
For example, after the user has clicked the button 3 times,
the label should say something like "3 clicks so far."
'''

from tkinter import *

class my_frame(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.button = Button(self, text = 'Click me!', command = self.print_message)
        self.button.grid(row = 0, column = 0)
        self.count = 0
        self.click_counter = Label(self, text = "0 clicks so far!")
        self.click_counter.grid(row = 1, column = 0)

    def print_message(self):
        self.count += 1
        self.click_counter['text'] = f'{self.count} clicks so far!'


# create new window and initialize and run the frame
root = Tk()
tnf = my_frame(root)
tnf.mainloop()