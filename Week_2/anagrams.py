'''The Jumble puzzle is a popular feature in many newspapers.
In a Jumble, the reader is presented with 5 or 6 letters that have
to be unscrambled to form a word. For example, the reader might be given DIWSMO,
and has to unscramble them to form the word WISDOM.

Modify your permute() function from part (a) to make a new function
anagrams() that returns a list of all the anagrams of an input string.
(An anagram of a string is a string with the same characters as the
original string, but in any order. For example, some anagrams of "stop"
are "pots", "tops", "spot", and "ostp".)

Then write a function jumble_solve() that takes as input a string and
returns a list of all the valid words that are anagrams of the input. 
Your output does not have to match the upper/lower case of the input.
(You should use your anagrams() function.) You can use the wordlist.txt
file to check the validity of words -- this file is at
http://artofproblemsolving.com/assets/pythonbook/_static/files/wordlist.txt'''

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

def anagrams(input):
    '''anagrams(input) -> list
    returns list of all correct anagrams of input'''
    inputList = []
    for i in range(len(input)) :
        inputList.append(input[i])
    if len(inputList) == 1 :
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