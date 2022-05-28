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


def angrms(input_list) :
    '''This code was adapted from the solution to problem 4 part a.
    My own code for that problem did work, but I think that the one
    given in the solution is more efficient and looks much less
    cluttered.'''
    if len(input_list) == 1:
        return [input_list[:]]
    # recursive step
    outputList = []  # to store permutations
    for index in range(len(input_list)):
        # construct all permutations that start with the item
        #   at location give by index
        # remove item and permute the rest
        restOfList = input_list[:index] + input_list[index+1:]
        perms = angrms(restOfList)
        # add all permutations starting with inputList[index]
        #   and ending with each permutation just generated
        for tail in perms:
            outputList.append([input_list[index]] + tail)
    return outputList

def anagrams(input):
    '''angrms(input) -> list
        returns list of all correct anagrams of input'''
    input_list = [char for char in input]
    words = angrms(input_list)
    perms = []
    text = open("wordlist.txt", "r")
    all_words = text.read().split("\n")
    for i in range(len(words)) :
        word = "".join(words[i])
        if word.lower() in all_words :
            perms.append(word)
    text.close()
    return list(set(perms))

# test cases
# print(angrms(["D", "I", "W", "S", "M", "O"]))
# print(anagrams("DIWSMO"))
# should print WISDOM


print(anagrams("CHWAT"))
# you get "WATCH"
print(anagrams("RAROM"))
# you get "ARMOR"
print(anagrams("CEPLIN"))
# you get "PENCIL"
print(anagrams("YAFLIM"))
# you get "FAMILY"