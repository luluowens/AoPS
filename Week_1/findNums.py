def findNums() :
    '''There are two 3-digit numbers n
    having the property that n is
    divisible by 11 and n/11 is equal
    to the sum of the squares of the
    digits of n.'''
    x = 0
    y = 0
    for n in range(100, 1000) :
        sum_of_digits = (n//100)*(n//100) + ((n % 100)//10)*((n % 100)//10) + (n%10)*(n%10)
        if n % 11 == 0 and sum_of_digits == n/11 :
            if x == 0 :
                x = n
            else :
                y = n
    print(str(x) + " and " + str(y))

findNums()