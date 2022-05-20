def get_base_number(num,base):
    '''get_base_number(num,base) -> int
    returns value of num as a base number in the given base'''
    if int(num) < 10 :
        return num
    return get_base_number(int(num) // 10, base) * base + (int(num) % 10)

# test cases
print(get_base_number('10011',2))  # should be 19
print(get_base_number('3202',5))   # should be 427
print(get_base_number('611023',7))  # should be 19