def maxScrabble() :
    '''finds the highest scoring
    7-lettered word from the
    file wordlist.txt'''
    values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1, 'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1, 'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
    text = open("wordlist.txt", "r")
    score = 0
    curr_score = 0
    word = ""
    for line in text :
        if len(line) == 8 :
            for char in line :
                if (not char == "z") and (not char == "\n"):
                    curr_score += values[char.upper()]
            if curr_score >= score :
                score = curr_score
                word = line
            curr_score = 0
    text.close()
    return word

print(maxScrabble())
    