def findLengthTen() :
    text = open("wordlist.txt", "r")
    count = 0
    for line in text :
        if len(line) == 11 :
            count += 1
    text.close()
    return count

print(findLengthTen())