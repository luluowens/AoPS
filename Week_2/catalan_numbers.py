'''The Catalan numbers are given by C_0 = 1 and the recursive formula
C_n = C_0 C_{n-1} + C_1 C_{n-2} + C_2 C_{n-3} + ... + C_{n-1} C_0.
In particular,
C_1 = C_0 C_0 = 1 * 1 = 1,
C_2 = C_0 C_1 + C_1 C_0 = 1 * 1 + 1 * 1 = 2,
C_3 = C_0 C_2 + C_1 C_1 + C_2 C_0 = 1 * 2 + 1 * 1 + 2 * 1 = 5,
C_4 = C_0 C_3 + C_1 C_2 + C_2 C_1 + C_3 C_0 = 1 * 5 + 1 * 2 + 2 * 1 + 5 * 1 = 14,
Write a Python program to compute C_{30}. Enter it as your answer below.'''

def catNum(degree) :
    '''catalan(n) -> int
    returns C_n, the nth Catalan number'''
    cat_list = [1, 1, 2]
    for i in range(2, degree + 1) :
        total = 0
        for j in range(i + 1) :
            total += cat_list[j] * cat_list[i - j]
        cat_list.append(total)
    return cat_list[degree]

print(catNum(30))