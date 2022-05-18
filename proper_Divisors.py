def properDivisors(num) :
    sumOfDivisors = 0
    for n in range(1, num) :
        if num % n == 0 :
            sumOfDivisors += n
    return sumOfDivisors

def findDouble() :
    for n in range(100, 1000) :
        if properDivisors(n) == 2 * n :
            print(n)
    return None

findDouble()