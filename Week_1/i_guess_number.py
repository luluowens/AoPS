def guessNumber() :
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