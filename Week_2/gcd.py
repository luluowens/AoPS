'''The greatest common divisor (or gcd) of two nonnegative integers
a and b (not both 0) is the largest positive integer that is a divisor
of both a and b. For example, the gcd of 20 and 45 is 5, since 5 divides
evenly into both 20 and 45, but no larger number divides them both.
The Euclidean algorithm is one way to find the gcd of two nonnegative integers.
It uses the facts that:
- gcd(a,0) = a for any positive integer a, and
- if a >= b, then gcd(a,b) = gcd(a-b,b).
Write a recursive function gcd() that takes two nonnegative integers
(not both 0) as input and uses the Euclidean algorithm to find the gcd of the inputs.'''

def gcd(a, b) :
    '''takes two nonnegative integers (not both 0)
    as input and uses the Euclidean algorithm
    to find the gcd of the inputs'''
    if a == 0 or b == 0 :
        return a + b
    else :
        if a >= b :
            return gcd(a-b, b)
        else :
            return gcd(a, b-a)

# print(gcd(45, 5))
# # should give you: 5
# print(gcd(9, 45))
# # should give you: 9
# print(gcd(5, 9))
# # should give you: 1
# print(gcd(6, 27))
# # should give you: 3