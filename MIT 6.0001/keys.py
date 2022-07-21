def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    count = 0
    big_val_key = None
    keys = aDict.keys()
    for key in keys :
        val = aDict[key]
        if len(val) >= count :
            big_val_key = key
            count = len(val)
    return big_val_key

dict = {'a': [15, 2], 'c': [18, 13, 10, 11, 10], 'b': [7, 3, 14, 1, 18, 5, 13, 10, 2, 11], 'd': [18]}
print(biggest(dict))