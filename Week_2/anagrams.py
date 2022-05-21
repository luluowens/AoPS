def anagrams(input):
    '''permute(inputList) -> list
    returns list of all permutations of inputList'''
    inputList = []
    for i in range(len(input)) :
        inputList.append(input[i])
    if inputList[1] == None :
        return inputList
    else :
        text = open("wordlist.txt", "r")
        permutations = []
        new_list = inputList[0 : -1]
        past_perms = anagrams(new_list)
        for perm in past_perms :
            for i in range(len(perm)) :
                word = perm.insert(i, inputList[-1])
                for line in text :
                    new_line = line.strip()
                    if word in new_line :
                        permutations.append(word)
        text.close()
        return permutations

# test cases
print(anagrams("CHWAT"))
# should print [[1,2], [2,1]] in some order
print(anagrams("RAROM"))
# should print [[1,2,3], [1,3,2], [2,1,3], [3,1,2], [2,3,1], [3,2,1]] in some order