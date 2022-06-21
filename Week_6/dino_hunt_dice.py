'''Implement the dice game Dino Hunt Dice with the following rules.
(This game is based on the game Dino Hunt Dice published by Steve Jackson Games.)

The game uses 13 colored 6-sided dice:
- 6 green dice: these have dinosaurs on 3 sides, leaves on 2 sides, and a foot on 1 side
- 4 yellow dice: these have dinosaurs on 2 sides, leaves on 2 sides and feet on 2 sides
- 3 red dice: these have dinosaurs on 1 side, leaves on 2 sides, and feet on 3 sides

The object is to capture as many dinosaurs as possible, while avoiding getting stomped.
The game runs for a predetermined number of turns, so that each player gets an equal number of turns.

On each turn:
- at the start of the turn, all 13 dice are placed into a pile
- the player randomly selects 3 dice and rolls them (if fewer than 3 dice are remaining,
the player rolls all the remaining dice)
- any dice showing dinosaurs and feet are set aside; any dice showing leaves are put back
into the pile of unrolled dice
- if the player has rolled 3 or more feet during the turn, the player has been stomped:
they lose all the dinosaurs captured during the turn and their turn ends.
- the player can stop and score 1 point for each dinosaur captured, or can continue rolling.

The player with the highest score wins.
'''

import random

### Die class that we previously wrote ###

class Die:
    '''Die class'''

    def __init__(self,sides=6):
        '''Die(sides)
        creates a new Die object
        int sides is the number of sides
        (default is 6)
        -or- sides is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sides,int):
            self.numSides = sides
            self.sides = list(range(1,sides+1))
        else:  # use the list/tuple provided 
            self.numSides = len(sides)
            self.sides = list(sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A '+str(self.numSides)+'-sided die with '+\
               str(self.get_top())+' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value

### end Die class ###

class DinoDie(Die):
    '''implements one die for Dino Hunt'''
    def __init__(self, color) :
        '''initializes a dino die with special faces
        '''
        self.color = color
        if color == "green" :   # green dino dice
            Die.__init__(self, sides = ["dino", "dino", "dino", "leaf", "leaf", "foot"])
        elif color == "yellow" :   # yellow dino dice
            Die.__init__(self, sides = ["dino", "dino", "leaf", "leaf", "foot", "foot"])
        else :   # red dino dice
            Die.__init__(self, sides = ["dino", "leaf", "leaf", "foot", "foot", "foot"])

    def __str__(self) :
        '''returns a string stating color and side up
        '''
        return f'   A {self.color} Dino Die with a {self.top} on top'


class DinoPlayer:
    '''implements a player of Dino Hunt'''
    def __init__(self, name) :
        '''initializes the player's name, sets their score to 0,
        creates an empty dice_hand list, and sets stomp to 0
        '''
        self.name = name
        self.score = 0
        self.stomp = 0

    def __str__(self) :
        '''returns the player's name and how many points they have
        '''
        return f'{self.name} has {self.score} points.'

    def play_turn(self, dice, dice_tops) :
        our_dice = dice
        our_tops = dice_tops
        dice_hand = []
        # start turn
        play = input("Press enter to select dice and roll.")
        # picks 3 dice
        if len(our_dice) < 3 :
            for die in our_dice :
                dice_hand.append(die)
        else :
            count = 0
            while count < 3 :
                die = our_dice[random.randint(0, len(dice)-1)]
                if die not in dice_hand :
                    dice_hand.append(die)
                    our_dice.remove(die)
                    die.roll()
                    print(die)
                    count += 1
        # checks for leaves
        for die in dice_hand :
            top = die.top
            if top == "leaf" :
                our_dice.append(die)
            elif top == "foot" :
                self.stomp += 1
            our_tops.append(top)
        # prints messages about roll situation
        print(f'This turn so far: {our_tops.count("dino")} dinos and {our_tops.count("foot")} feet')
        # removes dice with leaves from dice_hand
        for die in dice_hand :
            if die.top == "leaf" :
                dice_hand.remove(die)
        # checks if player is stomped
        if self.stomp >= 3 :
            print("Oh no, you got stomped!")
            self.stomp = 0
            return 0
        # if not stomped
        print(f'You have {len(our_dice)} dice remaining.')
        green = 0
        yellow = 0
        red = 0
        for die in our_dice :
            if die.color == "green" :
                green += 1
            elif die.color == "yellow" :
                yellow += 1
            else :
                red += 1
        print(f'{green} green, {yellow} yellow, {red} red')
        roll_again = input("Do you want to roll again? (y/n)")
        if roll_again == "y" :
            self.play_turn(our_dice, our_tops)
        else :
            self.stomp = 0
            self.score += our_tops.count("dino")


def play_dino_hunt(numPlayers,numRounds):
    '''play_dino_hunt(numPlayer,numRounds)
    plays a game of Dino Hunt
      numPlayers is the number of players
      numRounds is the number of turns per player'''
    # set up 13 dice
    dice_pile = []
    for i in range(6) :   # creates 6 green dino dice
        dice_pile.append(DinoDie("green"))
    for i in range(4) :   # creates 4 yellow dino dice
        dice_pile.append(DinoDie("yellow"))
    for i in range(3) :   # creates 3 red dino dice
        dice_pile.append(DinoDie("red"))

    # set up players
    players = []
    for i in range(numPlayers) :
        name = input(f'Player {i + 1}, enter your name: ')
        players.append(DinoPlayer(name))
    
    # play game
    for i in range(numRounds) :
        print(f'ROUND {i + 1}')
        for player in players :
            print(player)
        for player in players :
            print(player.name + ", it's your turn!")
            player.play_turn(dice_pile, [])
    
    # end game
    print("The game has ended. We have a winner!")
    winning_val = 0
    for player in players :
        if player.score > winning_val :
            winning_val = player.score
    for player in players :
        if player.score == winning_val :
            print(player)


play_dino_hunt(2,1)