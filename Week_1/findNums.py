def findNums() :
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