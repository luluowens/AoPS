def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    while True :
        new_list = []
        any_lists_left = False
        for value in aList :
            if type(value) is list :
                for element in value :
                    new_list.append(element)
                any_lists_left = True
            else :
                new_list.append(value)
        if any_lists_left == False :
            return aList
        else :
            aList = new_list


aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flatten(aList))