'''Elevators transport people! Let's add that functionality to our Elevator class.
Modify our Elevator class from this week's lesson as follows:
Add an attribute passengers that is a list of strings representing the names of the people.
(This will also require modifying the constructor method -- new elevators should start
out empty of passengers.)
Modify the __str__() method to also print the names of the passengers.
Add methods get_on() and get_off() to allow passengers to get on and off.
Of course, passengers can only get on and off if the doors are open!
Make sure your methods do something appropriate if the doors are closed
(for example, printing a message to that effect).
Also make sure that get_off() does something appropriate if that person is not on the elevator.
Be sure to write some examples to test your modifications.
'''

class Elevator:
    '''Represents a simple elevator'''

    def __init__(self, startFloor, startDoorsOpen):
        '''Elevator(startFloor, startDoorsOpen) -> Elevator
        Constructs an Elevator
        startFloor: int giving the starting floor
        startDoorsOpen: bool giving the starting doors 
                    (True = 'open')'''
        self.floor = startFloor  # store floor attribute
        self.doorsOpen = startDoorsOpen  # store doors attribute
        self.passengers = [] # store passengers attribute

    def __str__(self):
        '''str(Elevator) -> str
        Returns a string giving the floor and state of the doors.'''
        answer = 'doors '         # will contain string to return
        if self.doorsOpen:        # if doors open
            answer += 'open'      # say so
        else:                     # if doors closed
            answer += 'closed'    # say that too
        answer += ', floor '      # this is in every answer
        answer += str(self.floor) # add floor number
        answer += ", with passengers "
        for i in range(len(self.passengers) - 1) :
            answer += self.passengers[i] + ", "
        answer += "and " + self.passengers[-1] + "."
        return answer

    def open_doors(self):
        '''Elevator.open_doors()
        Opens the doors by setting doors attribute to True.'''
        self.doorsOpen = True # set doors to open

    def close_doors(self):
        '''Elevator.close_doors()
        Closes the doors by setting doors attribute to False.'''
        self.doorsOpen = False # set doors to closed

    def go_up(self):
        '''Elevator.go_up()
        Goes up by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor += 1              # increase floor by 1

    def go_down(self):
        '''Elevator.go_down()
        Goes down by one floor if doors are not open.'''
        if self.doorsOpen:               # if doors are open
            print('Please close doors!') # print warning
        else:                            # if doors are closed
            self.floor -= 1              # decrease floor by 1

    def go_to_floor(self, destination):
        '''Elevator.go_to_floor(int)
        Closes doors, moves to destination, and opens doors.'''
        if self.doorsOpen:               # if doors are open
            self.close_doors()           # close 'em
        while self.floor != destination: # if not at destination
            if self.floor < destination: # if below
                self.go_up()             # go up 1 floor
            else:                        # if above
                self.go_down()           # go down 1 floor
        self.open_doors()                # open doors

    def get_on(self, passenger) :
        if self.doorsOpen :
            self.passengers.append(passenger)
            self.doorsOpen = False
        else :
            print("Please open doors for passenger to get on!")
    
    def get_off(self, passenger) :
        if self.doorsOpen :
            if passenger in self.passengers :
                self.passengers.append(passenger)
                self.doorsOpen = False
            else :
                print("This passenger is not on the elevator!")
        else :
            print("Please open doors for passenger to get on!")