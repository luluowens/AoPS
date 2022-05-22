'''Write a program that implements the reverse of the
simple guessing game in part (a). In this game, the human
player will randomly select an integer between 0 and 100 (inclusive),
and the computer will repeatedly try to guess the person's number.
The player will tell the computer whether its guess is too high or
too low, and will tell the computer when it's guessed the exact number.
The program should also output the number of guesses that it took the
computer to guess the correct number.
'''

def guessNumber() :
    '''reverse_guessing_game(n) -> int
    plays the reverse guessing game
    Player pick a number between 0 and n (inclusive)
    Computer tries to guess the number
    Returns the number of guesses it takes'''
    count = 0
    left = 0
    right = 100
    
    while left < right :
        mid = left + (right - left) // 2
        print("I guess " + str(mid))
        count += 1
        l_or_h = str(input("Is this high, low, or correct? "))
        if l_or_h == "low" :
            left = mid + 1
        elif l_or_h == "high" :
            right = mid - 1
        else :
            print("I knew it!")
            break
    
    print("It took me " + str(count) + " guesses")
    return None

print("Think of a number between 0 and 100")
print("Hit enter when you have it.")
guessNumber()