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

# import re

def angrms(input_list) :
        '''angrms(input) -> list
        returns list of all correct anagrams of input'''
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
    input_list = []
    for i in range(len(input)) :
        input_list.append(input[i])
    words = angrms(input_list)
    # corr_words = []
    # for i in range(len(words)) :
    #     word = "".join(words[i])
    #     corr_words.append(word)
    # p = "^" + "|".join(corr_words)
    perms = []
    text = open("wordlist.txt", "r")
    all_words = text.read()
    poss_words = all_words.split("\n")
    for i in range(len(words)) :
        word = "".join(words[i])
        if word.lower() in poss_words :
            perms.append(word)
    text.close()
    return list(set(perms))

# test cases
# print(angrms(["D", "I", "W", "S", "M", "O"]))
# print(anagrams("DIWSMO"))
# should print WISDOM


print(anagrams("CHWAT"))
print(anagrams("RAROM"))
print(anagrams("CEPLIN"))
print(anagrams("YAFLIM"))