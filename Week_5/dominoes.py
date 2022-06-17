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
        val = random.randint(28)
        return self.deck.pop(val)


class Chain:
    def __init__(self) :
        self.chain = []
    
    def __str__(self) :
        ans = ""
        for i in range(len(self.chain) - 1) :
            ans += self.chain[i] + ", "
        return ans + self.chain[len(self.chain) - 1]

    def add_dom(self, dom, side) :
        if side == "left" :
            temp = self.chain
            self.chain = dom + temp
        else :
            self.chain += dom


# player class
class Player:
    def __init__(self, deck, player_num) :
        '''initializes a player with their "hand" of 7 dominoes
        '''
        self.hand = [deck.deal_domino() for i in range(7)]
        self.num = player_num

    def __str__(self) :
        '''returns a string stating the number of dominoes the player currently has
        '''
        return f'You have {len(self.deck)} dominoes left'

    def can_move(self, chain) :
        for dom in self.hand :
            if dom.val1 == chain[0] or dom.val2 == chain[0] or dom.val1 == chain[-1] or dom.val2 == chain[-1] :
                return dom
        return None

    def move(self, dom, chain) :
        if dom.val1 == chain[0] :
            chain.add_dom([dom.val2, dom.val1], "left")
        elif dom.val2 == chain[0] :
            chain.add_dom([dom.val1, dom.val2], "left")
        elif dom.val1 == chain[-1] :
            chain.add_dom([dom.val1, dom.val2], "right")
        else :
            chain.add_dom([dom.val2, dom.val1], "right")


# game
def playDominoes() :
    deck = Deck()
    chain = Chain()
    human_player = Player(deck, 0)
    welcome_message = "Hello! These are your dominoes: "
    for dom in range(len(human_player.hand) - 1) :
        welcome_message += dom + ", "
    print(welcome_message + human_player.hand[-1])
    comp_player1 = Player(deck, 1)
    comp_player2 = Player(deck, 2)
    comp_player3 = Player(deck, 3)
    players = [human_player, comp_player1, comp_player2, comp_player3]
    curr_player = 0
    while True:
        player = players[curr_player]
        if player.has_won() :
            if player == human_player :
                print("Congratulations! You won!")
            else :
                print("Sorry, but you lost. Try again next time.")
            break
        else :
            count = 0
            for i in range(4) :
                if not players[i].can_move() :
                    count += 1
            if count == 4 :
                break
        if player.can_move() :
            player.play()
        curr_player = (curr_player + 1) % 4
