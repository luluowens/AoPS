def is_power(x, p):
    """
    x: an int
    p: an int > 0
    Returns True if there exists a positive int, i, such that p**i == x, and False otherwise.
    """
    i = 1
    while p ** i <= x :
        if p ** i == x :
            return True
        elif p ** i == p ** (i-1) :
            return False
        i += 1
    return False


# testing
print(is_power(4,2))   # prints True
print(is_power(5,2))   # prints False
print(is_power(-4,2))  # prints False
print(is_power(9,3))  # prints True
print(is_power(15,3))  # prints False
print(is_power(3,1))  # prints False
print(is_power(1,5))  # prints False
print(is_power(125,5))  # prints True