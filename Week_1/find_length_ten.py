def findLengthTen() :
    '''finds the number of words
    that have a length of ten
    in the file wordlist.txt'''
    text = open("wordlist.txt", "r")
    count = 0
    for line in text :
        if len(line) == 11 :
            count += 1
    text.close()
    return count

print(findLengthTen())