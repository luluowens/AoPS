def is_formed_by_s(s1, s2):
    """ s1 and s2 are strings containing lowercase alphabetic characters
        Returns True if s2 can be formed using the letters in s1 
        in the order in which they appear in s1. """
    letters_available = s1
    for letter in s2 :
        location = letters_available.find(letter)
        if location == -1 :
            return False
        else :
            letters_available = s1[location+1:]
    return True


# testing
print(is_formed_by_s('abcd', 'bcd')) # prints True
print(is_formed_by_s('abcd', 'ad')) # prints True
print(is_formed_by_s('abcd', 'ba')) # prints False
print(is_formed_by_s('abbcd', 'bbcaa')) # prints False
print(is_formed_by_s('abbcd', 'bbc')) # prints True
print(is_formed_by_s('abcd', 'xyz')) # prints False