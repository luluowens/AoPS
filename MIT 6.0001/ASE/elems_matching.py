def elems_matching(L1, L2, f):
    """ L1 is a non-empty list containing unique ints
        L2 is a non-empty list containing ints, of the same length as L1
        f is a function that takes in an int and returns an int

    Returns a dictionary that maps an element at index i from L1 to an 
    element at index i in L2. The only key-value pairs in the dict are 
    those at index i where f applied to L1 at index i equals L2 at index i.
    """
    map = {}
    for i in range(len(L1)) :
        if f(L1[i]) == L2[i] :
            map[L1[i]] = L2[i]
    return map



# testing
L1 = [1,2,3]
L2 = [2,3,2]
def f(a):
    return a+1
print(elems_matching(L1, L2, f))  # prints {1: 2, 2: 3}

L1 = [0,3,7,9]
L2 = [0,0,0,9]
def f(a):
    return 0
print(elems_matching(L1, L2, f))  # prints {0: 0, 3: 0, 7: 0}

L1 = [1,2,3,4]
L2 = [1,4,27,16]
def f(a):
    return a ** 2
print(elems_matching(L1, L2, f))  # prints {1: 1, 2: 4, 4: 16}