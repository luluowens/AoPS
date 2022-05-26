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
        last_char = inputList.pop()
        past_perms = permute(inputList)
        if len(past_perms) == 1 :
            return [past_perms + [last_char], [last_char] + past_perms]
        for perm in past_perms :
            for i in range(len(perm) + 1) :
                new_perm = perm[0:i] + [last_char] + perm[i: len(perm) + 1]
                permutations.append(new_perm)
        return permutations

# test cases
print(permute([1,2]))
# should print [[1,2], [2,1]] in some order
print(permute([1,2,3]))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order