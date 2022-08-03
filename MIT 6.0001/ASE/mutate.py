def mutate_if_formed_by_L(L1, L2):
    """ L1 and L2 are lists containing ints
        Determines if the elements in L2 can be formed using the 
        elements in L1 in the order in which they appear in L1. 
        If yes, mutates L1 to contain the same elements in L2. 
        If no, L1 stays unchanged. 
        Returns None."""
    ints_available = L1.copy()
    not_formed = False
    for integer in L2 :
        if integer not in ints_available :
            not_formed = True
            return None
        else :
            location = ints_available.index(integer)
            ints_available = ints_available[location+1:]
    if not_formed == False :
        i = 0
        while i < len(L1) :
            if L1[i] not in L2 :
                L1.remove(L1[i])
            else :
                i += 1
    return None
        

# testing
La = [1,2,3,4]
Lb = [2,3,4]
mutate_if_formed_by_L(La, Lb)
print(La)   # prints [2, 3, 4]

La = [1,2,3,4]
Lb = [1,4]
mutate_if_formed_by_L(La, Lb) 
print(La)   # prints [1, 4]

La = [1,2,3,4]
Lb = [2,1]
mutate_if_formed_by_L(La, Lb) 
print(La)   # prints [1, 2, 3, 4]