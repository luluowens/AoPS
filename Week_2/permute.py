'''Write a recursive function permute() whose argument is a list.
The function should return a list of all possible re-orderings
(also called permutations) of the argument. That is, the function
should return a list of lists.'''

def permute(inputList):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    if len(inputList) == 1 :
        return inputList
    else :
        permutations = []
        new_list = inputList[0 : -1]
        past_perms = permute(new_list)
        for j in len(past_perms) :
            for i in range(len(past_perms[j])) :
                permutations.append(past_perms[j].insert(i, inputList[-1]))
        return permutations

# test cases
print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order