def prime_factorization(num) :
    '''prime_factorization(num) -> str
    returns a string with the prime factorization of num
    num: int
    '''
    primes = {} # dictionary to keep track of the primes
    divisor = 2 # keep track of the divisor

    while num > 1:
        divisorCount = 0 # keeps track of how many times we can divide divisor into num
        while num % divisor == 0 :  # divisor is a factor
            num = num // divisor
            divisorCount += 1

        if divisorCount > 0:   # if we had any, add a dict entry
            primes[divisor] = divisorCount

        divisor += 1  # increment the divisor

    divisor += 1  # increment the divisor

    # process the output
    # sort the primes
    primeList = list(primes.keys())
    primeList.sort()
    output = ''  # initialize output string

    for prime in primeList:
        output += str(prime) 
        if primes[prime] > 1:  # need to add an exponent
            output += '^' + str(primes[prime])
        output += ' * ' # add multiplication symbol

    # don't output the last multiplication symbol   
    return output[: -3]

print(prime_factorization(600))