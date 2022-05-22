import random

'''Write a program that implements a simple guessing game.
The computer will randomly select an integer between 0 and 100 (inclusive),
and the user will repeatedly try to guess the computer's number.
The computer will tell the player whether her guess is too high or too low,
and will tell the user when she's guessed the exact number.
The program should also output the number of guesses that it took the
player to guess the correct number.'''

def guessNumber() :
    '''guessing_game(n) -> int
    plays a guessing game
    Computer picks a number between 0 and n (inclusive)
    Returns the number of guesses it takes'''
    num = int(random.randrange(100))
    count = 0
    
    def guess(count) :
        val = int(input("Enter your guess: "))
        if val < num :
            print("Sorry, " + str(val) + " is too low.")
            count += 1
            guess(count)
        elif val > num :
            print("Sorry, " + str(val) + " is too high.")
            count += 1
            guess(count)
        elif val == num :
            print("Good job! " + str(val) + " is my number.")
            print("It took you " + str(count) + " guesses.")

    guess(count)

print("I'm thinking of a number between 0 and 100")
guessNumber()