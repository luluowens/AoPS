'''Using object-oriented programming, write a Python program to play dominoes.

A domino set consists of 28 tiles: each tile has two numbers from 0 to 6,
and every possible combination appears once. Note that a set includes 7 "double" dominoes
(from 0-0 through 6-6) and 21 dominos with two different numbers.

The game is for 4 players: each player gets 7 dominoes.
The player with the double-6 domino goes first and must play it -- that starts the chain.
Then, in turn, each player must play a domino to add to the chain;
the new domino can match either end of the chain. For example, if the chain is 1-2,2-6,6-6,6-5,
then the player can play any domino with a 1 (on the left side of the chain) or a
5 (on the right side of the chain). A player who cannot play must pass.
The player who plays his/her final domino wins; if the game is blocked so that no one can play,
then the last player who was able to play wins.

Implement the game as a solitaire game with a single human player and three computer-controlled opponents.
The player should be able to see his/her own dominoes, and the entire chain,
but naturally cannot see the computer players' dominoes.
'''
import random


# domino class
class Domino:
    def __init__(self, val1, val2) :
        '''initialize the values of a domino
        these two values need to be a number from 0 to 6
        '''
        self.val1 = val1
        self.val2 = val2
    
    def __str__(self) :
        '''returns a string for the domino
        Eg. "1, 2"
        '''
        return f'{self.val1}, {self.val2}'


# deck class
class Deck:
    def __init__(self) :
        '''initialize the deck of dominoes with all of the possible values
        '''
        self.deck = []
        for i in range(7) :
            for j in range(i, 7) :
                self.deck.append(Domino(i, j))
        random.shuffle(self.deck)  # shuffle the deck
    
    def __str__(self) :
        '''returns a string stating the number of dominoes left in deck
        '''
        return 'An deck of dominoes with '+str(len(self.deck))+' dominoes remaining.'
    
    def is_empty(self) :
        '''check if deck is empty
        '''
        return len(self.deck) == 0

    def deal_domino(self) :
        '''deals out 1 domino
        '''
        return self.deck[random.randint(28)]


class Chain:
    def __init__(self) :
        # code
        return 0
    
    def __str__(self) :
        # code
        return 0


# player class
class Player:
    def __init__(self, deck) :
        '''initializes a player with their "hand" of 7 dominoes
        '''
        self.hand = [deck.deal_domino() for i in range(7)]

    def __str__(self) :
        '''returns a string stating the number of dominoes the player currently has
        '''
        return f'You have {len(self.deck)} dominoes left'

    def play(self) :
        # code 
        return 0


# computer class
class Computer:
    def __init__(self) :
        # code
        return 0

    def __str__(self) :
        # code
        return 0
    

# game
def playDominoes() :
    # code
    return 0