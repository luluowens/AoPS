def remove_letter(string, letter):
    '''remove_letter(string,letter) -> str
    returns string with all occurrences of letter removed'''
    newString = ""
    for char in string :
        if not char == letter :
            newString += char
    return newString

# test cases
print(remove_letter('This is a test','t'))  # should print 'This is a es'
print(remove_letter('Hello World!','l'))    # should print 'Heo Word!'
print(remove_letter('I like Python','q'))   # should print 'I like Python'