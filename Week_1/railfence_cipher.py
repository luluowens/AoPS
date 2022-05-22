'''Part (a): Write a function encipher_fence.
It takes two parameters: the first is a string to scramble,
and the second is the number of rails. It should return the scrambled text.

Part (b): Write a function decipher_fence.
It takes two parameters: the first is a string to unscramble,
and the second is the number of rails. It should return the original text.

Part (c): Write a function decode_text.
It should take two parameters, a text to decode and a filename
for a file containing a list of English words.
It should return a deciphered text, reversing the railfence cipher.
This would be easy if you knew the number of rails involved.
Without that knowledge, you can still break the code:
try different rail numbers (2, 3, 4, etc.) until you get a text that
consists of English words. (You can assume that the number of rails will
not be more than 10.) Not every word in the coded text may appear in
the wordlist (for example, proper names). You should return the text
with the most words in it, according to your list of valid words.
Also make sure you ignore punctuation when you look up words in the word list.
You can use the file wordlist.txt to check the validity of words.'''

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
    text = open(wordfilename, "r")
    all_words = text.read()
    all_words.split("\n")
    for i in range(2, 11) :
        new_text = decipher_fence(ciphertext, i)
        words = new_text.split()
        for word in words :
            if word.strip(",.!?") in all_words :
                count += 1
        if count >= max :
            deciphered = new_text
            max = count
        count = 0
    text.close()
    return deciphered

# test cases

# # enciphering
# print(encipher_fence("abcdefghi", 3))
# # should print: cfibehadg
# print(encipher_fence("This is a test.", 2))
# # should print: hsi  etTi sats.
# print(encipher_fence("This is a test.", 3))
# # should print: iiae.h  ttTss s
# print(encipher_fence("Happy birthday to you!", 4))
# # should print: pidtopbh ya ty !Hyraou

# # deciphering
# print(decipher_fence("dcgbfae",4))
# # should print: abcdefg
# print(decipher_fence("hsi  etTi sats.",2))
# # should print: This is a test.
# print(decipher_fence("iiae.h  ttTss s",3))
# # should print: This is a test.
# print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# # should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print: It's fun learning Python in an AoPS class.