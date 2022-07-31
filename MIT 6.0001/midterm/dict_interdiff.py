'''Assume you are given two dictionaries d1 and d2, each with integer keys and integer values.
You are also given a function f, that takes in two integers, performs an unknown operation
on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
The function will return a tuple of two dictionaries: a dictionary of the intersect of
d1 and d2 and a dictionary of the difference of d1 and d2, calculated as follows:

intersect: The keys to the intersect dictionary are keys that are common in both d1 and d2.
To get the values of the intersect dictionary, look at the common keys in d1 and d2 and
apply the function f to these keys' values -- the value of the common key in d1 is the
first parameter to the function and the value of the common key in d2 is the second parameter
to the function. Do not implement f inside your dict_interdiff code -- assume it is defined
outside.

difference: a key-value pair in the difference dictionary is (a) every key-value pair
in d1 whose key appears only in d1 and not in d2 or (b) every key-value pair in d2 whose
key appears only in d2 and not in d1.
'''

def f(a, b) :
    return a > b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = {}
    difference = {}
    for key_1 in d1 :
        if key_1 in d2 :
            intersect[key_1] = f(d1[key_1], d2[key_1])
        else :
            difference[key_1] = d1[key_1]
    for key_2 in d2 :
        if key_2 not in d1 :
            difference[key_2] = d2[key_2]
    return (intersect, difference)

# d1 = {1:30, 2:20, 3:30, 5:80}
# d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
print(dict_interdiff(d1, d2))
