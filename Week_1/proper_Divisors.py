'''A proper divisor of a positive integer n is a positive integer
d < n such that d divides n evenly, or alternatively if n is a multiple of d.
For example, the proper divisors of 12 are 1, 2, 3, 4, and 6, but not 12.
A positive integer $n$ is called double-perfect if the sum of its
proper divisors equals 2n. For example, 120 is double-perfect
(and in fact is the smallest double-perfect number) because its
proper divisors are 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, and 60,
and their sum is 240, which is twice 120. There is only one other 3-digit
double-perfect number.'''

def properDivisors(num) :
    '''find sum of the proper divisors
    of num'''
    sumOfDivisors = 0
    for n in range(1, num) :
        if num % n == 0 :
            sumOfDivisors += n
    return sumOfDivisors

def findDouble() :
    '''finds the number whose
    sum of the proper divisors
    is twice the number'''
    for n in range(100, 1000) :
        if properDivisors(n) == 2 * n :
            print(n)
    return None

findDouble()