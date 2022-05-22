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