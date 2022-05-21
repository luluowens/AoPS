def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    if inputList[1] == None :
        return inputList
    else :
        permutations = []
        new_list = inputList[0 : -1]
        past_perms = permute(new_list)
        for perm in past_perms :
            for i in range(len(perm)) :
                permutations.append(perm.insert(i, inputList[-1]))
        return permutations

# test cases
print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order