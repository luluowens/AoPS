def encipher_fence(plaintext,numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    new_text = ""
    while len(new_text) < len(plaintext) :
        for j in range(numRails) :
            for i in range(len(plaintext)):
                if i % numRails == numRails - 1 - j :
                    new_text += plaintext[i]
    return new_text

def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    new_text = [""] * len(ciphertext)
    start = numRails - 1
    index = start
    for i in range(len(ciphertext)) :
        if index >= len(ciphertext) :
            index = start - 1
            new_text[index] = ciphertext[i]
            start -= 1
        else :
            new_text[index] = ciphertext[i]
        index += numRails
    return ''.join(new_text)

def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    count = 0
    max = 1
    deciphered = ""
    for i in range(2, 11) :
        text = open(wordfilename, "r")
        words = []
        word = ""
        new_text = decipher_fence(ciphertext, i)
        for val in range(len(new_text)) :
            if new_text[val] == " " :
                words.append(word)
                word = ""
            elif new_text[val] != "," or new_text[val] != "." :
                word += new_text[val]
        words.append(word)
        for line in text :
            for word in words :
                new_line = line.strip()
                if word == new_line :
                    count += 1
        if count >= max :
            deciphered = new_text
            max = count
        count = 0
        text.close()
    return deciphered

# test cases

enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("dcgbfae",4))
# should print: abcdefg
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print: It's fun learning Python in an AoPS class.