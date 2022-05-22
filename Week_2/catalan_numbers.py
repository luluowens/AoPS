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