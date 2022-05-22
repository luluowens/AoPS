import random

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