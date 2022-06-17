'''Rules for simple Uno:

- Played with a deck of 76 cards --
there's one 0 and two of each of 1-9 in each of four colors (red, blue, yellow, green).

- Each player gets 7 cards.

- A single card from the deck is turned face up to start a discard pile.

- Each player, in turn, must play a card that matches the top card of the discard pile
either in number or in color. (For example, if the top card is "red 4", a player could play "red 9"
or "blue 4".) The played card goes on top of the pile.

- If a player can't play, they draw a card from the deck. If they can play the card just drawn,
they do so; otherwise they add it to their hand. In either case, the player's turn is over.

- If the deck runs out, we shuffle the discard pile (except for the top card) and use it as our new deck.

- The first player to get rid of all of their cards wins.

Write the Uno game using classes.

Add the action cards to our Uno game.
There are three types of action cards, and the deck should have 2 of each type of each color
(so this adds 24 cards total to the deck):

Skip: when played, the next player's turn is skipped.

Reverse: when played, the order of play gets reversed.
For example, if player #3 plays Reverse, then player #2 goes next, then player #1,
and so on, until another Reverse is played, at which time the order of play gets reversed again
back to the "normal order".

Draw Two: when played, the next player must draw 2 cards, and his/her turn is skipped.

These cards have the same matching rules as regular cards: for example, if when it comes to
my turn there's a blue Skip on top of the pile, then I could play a green Skip, or a blue 2,
or any other card that is a Skip or is blue.
'''

import random

class UnoCard:
    '''represents an Uno card
    attributes:
      rank: int from 0 to 9 or action cards (skip, reverse, draw 2)
      color: string'''

    def __init__(self,rank,color):
        '''UnoCard(rank,color) -> UnoCard
        creates an Uno card with the given rank and color'''
        self.rank = rank
        self.color = color

    def __str__(self):
        '''str(Unocard) -> str'''
        return(str(self.color)+' '+str(self.rank))

    def is_match(self,other):
        '''UnoCard.is_match(UnoCard) -> boolean
        returns True if the cards match in rank or color, False if not'''
        return (self.color == other.color) or (self.rank == other.rank)

class UnoDeck:
    '''represents a deck of Uno cards
    attribute:
      deck: list of UnoCards'''

    def __init__(self):
        '''UnoDeck() -> UnoDeck
        creates a new full Uno deck'''
        self.deck = []
        for color in ['red', 'blue', 'green', 'yellow']:
            self.deck.append(UnoCard(0,color))  # one 0 of each color
            for n in range(1,10):  # two of each of 1-9 of each color
                self.deck.append(UnoCard(n,color))
        random.shuffle(self.deck)  # shuffle the deck

    def __str__(self):
        '''str(Unodeck) -> str'''
        return 'An Uno deck with '+str(len(self.deck))+' cards remaining.'

    def is_empty(self):
        '''UnoDeck.is_empty() -> boolean
        returns True if the deck is empty, False otherwise'''
        return len(self.deck) == 0

    def deal_card(self):
        '''UnoDeck.deal_card() -> UnoCard
        deals a card from the deck and returns it
        (the dealt card is removed from the deck)'''
        return self.deck.pop()

    def reset_deck(self,pile):
        '''UnoDeck.reset_deck(pile) -> None
        resets the deck from the pile'''
        if len(self.deck) != 0:
            return
        self.deck = pile.reset_pile() # get cards from the pile
        random.shuffle(self.deck)  # shuffle the deck

class UnoPile:
    '''represents the discard pile in Uno
    attribute:
      pile: list of UnoCards'''

    def __init__(self,deck):
        '''UnoPile(deck) -> UnoPile
        creates a new pile by drawing a card from the deck'''
        card = deck.deal_card()
        self.pile = [card]  # all the cards in the pile

    def __str__(self):
        '''str(UnoPile) -> str'''
        return 'The pile has '+str(self.pile[-1])+' on top.'

    def top_card(self):
        '''UnoPile.top_card() -> UnoCard
        returns the top card in the pile'''
        return self.pile[-1]

    def add_card(self,card):
        '''UnoPile.add_card(card) -> None
        adds the card to the top of the pile'''
        self.pile.append(card)

    def reset_pile(self):
        '''UnoPile.reset_pile() -> list
        removes all but the top card from the pile and
          returns the rest of the cards as a list of UnoCards'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck

class UnoPlayer:
    '''represents a player of Uno
    attributes:
      name: a string with the player's name
      hand: a list of UnoCards'''

    def __init__(self,name,deck):
        '''UnoPlayer(name,deck) -> UnoPlayer
        creates a new player with a new 7-card hand'''
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]

    def __str__(self):
        '''str(UnoPlayer) -> UnoPlayer'''
        return str(self.name)+' has '+str(len(self.hand))+' cards.'

    def get_name(self):
        '''UnoPlayer.get_name() -> str
        returns the player's name'''
        return self.name

    def get_hand(self):
        '''get_hand(self) -> str
        returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output

    def has_won(self):
        '''UnoPlayer.has_won() -> boolean
        returns True if the player's hand is empty (player has won)'''
        return len(self.hand) == 0

    def draw_card(self,deck):
        '''UnoPlayer.draw_card(deck) -> UnoCard
        draws a card, adds to the player's hand
          and returns the card drawn'''
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self,card,pile):
        '''UnoPlayer.play_card(card,pile) -> None
        plays a card from the player's hand to the pile
        CAUTION: does not check if the play is legal!'''
        self.hand.remove(card)
        pile.add_card(card)

    def take_turn(self,deck,pile,players):
        '''UnoPlayer.take_turn(deck,pile) -> None
        takes the player's turn in the game
          deck is an UnoDeck representing the current deck
          pile is an UnoPile representing the discard pile'''
        # print player info
        print(self.name+", it's your turn.")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
        # get a list of cards that can be played
        topcard = pile.top_card()
        matches = [card for card in self.hand if card.is_match(topcard)]
        if len(matches) > 0:  # can play
            for index, matches[index] in range(len(matches)):
                # print the playable cards with their number
                print(str(index+1) + ": " + str(matches[index]))
            # get player's choice of which card to play
            choice = 0
            while choice < 1 or choice > len(matches):
                choicestr = input("Which do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            # play the chosen card from hand, add it to the pile
            self.play_card(matches[choice-1],pile)
        else:  # can't play
            print("You can't play, so you have to draw.")
            input("Press enter to draw.")
            # check if deck is empty -- if so, reset it
            if deck.is_empty():
                deck.reset_deck(pile)
            # draw a new card from the deck
            newcard = self.draw_card(deck)
            print("You drew: "+str(newcard))
            # check if card is a skip card
            if newcard.rank == "skip" :
                if newcard.is_match(topcard) :
                    print("Good -- you can play that!")
                    self.play_card(newcard,pile)
                    players.skip_player()
                else:   # still can't play
                    print("Sorry, you still can't play.")
            # check if card is a reverse card
            elif newcard.rank == "reverse" :
                if newcard.is_match(topcard) :
                    print("Good -- you can play that!")
                    self.play_card(newcard,pile)
                    players.reverse_player()
                else:   # still can't play
                    print("Sorry, you still can't play.")
            # check if card is a draw 2 card
            elif newcard.rank == "reverse" :
                if newcard.is_match(topcard) :
                    print("Good -- you can play that!")
                    self.play_card(newcard,pile)
                    players.draw_two(deck)
                else:   # still can't play
                    print("Sorry, you still can't play.")
            # for regular cards
            elif newcard.is_match(topcard): # can be played
                print("Good -- you can play that!")
                self.play_card(newcard,pile)
            else:   # still can't play
                print("Sorry, you still can't play.")
            input("Press enter to continue.")

class Players:
    def __init__(self) :
        '''initializes an empty player list
        '''
        self.playerList = []
        self.currPlayer = 0
        self.nextPlayer = None

    def __str__(self) :
        '''returns the names of the players
        '''
        ans = ""
        for i in range(len(self.playerList) - 1) :
            ans += self.chain[i] + ", "
        return ans + self.chain[len(self.playerList) - 1]

    def add_player(self, player) :
        self.playerList.append(player)

    def skip_player(self) :
        self.currPlayer += 2
        self.nextPlayer += 2

    def reverse_player(self) :
        length = len(self.playerList)
        self.playerList = [self.playerList[length - x - 1] for x in range(length)]

    def draw_two(self, deck) :
        self.playerList[self.currPlayer + 1].draw_card(deck)
        self.currPlayer += 2
        self.nextPlayer += 2
        

def play_uno(numPlayers):
    '''play_uno(numPlayers) -> None
    plays a game of Uno with numPlayers'''
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    players = Players()
    for n in range(numPlayers):
        # get each player's name, then create an UnoPlayer
        name = input('Player #'+str(n+1)+', enter your name: ')
        players.add_player(UnoPlayer(name,deck))
    # randomly assign who goes first and who goes next
    players.currPlayer = random.randrange(numPlayers)
    players.nextPlayer = players.currPlayer + 1
    # play the game
    while True:
        # print the game status
        print('-------')
        for player in players.playerList:
            print(player)
        print('-------')
        # take a turn
        players.playerList[players.currPlayer].take_turn(deck,pile,players.playerList)
        # check for a winner
        if players.playerList[players.currPlayer].has_won():
            print(players.playerList[players.currPlayer].get_name()+" wins!")
            print("Thanks for playing!")
            break
        # go to the next player
        players.currPlayer = (players.currPlayer + 1) % numPlayers