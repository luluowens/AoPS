def occurs_most_often(L):
    """
    L: a list of ints
    Returns the element in L that occurs the most often in L.
    In case of a tie, returns the maximum of the tied values.
    Raises a ValueError if L is empty.
    """
    if len(L) == 0 :
        raise ValueError("Your list L is empty!")
    else :
        max_val = L[0]
        max_count = 1
        for value in L :
            curr_count = L.count(value)
            if curr_count > max_count :
                max_val = value
                max_count = curr_count
            elif curr_count == max_count :
                max_val = max(max_val, value)
        return max_val


# testing
print(occurs_most_often([1,2,1]))          # prints 1
print(occurs_most_often([6,6,2,2]))        # prints 6
print(occurs_most_often([6,0,6,2,0,2,0]))  # prints 0
print(occurs_most_often([0,6,6,6,2,0,2,0,2]))  # prints 6
print(occurs_most_often([]))  # raises a ValueError