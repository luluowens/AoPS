def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    run_sum = 0
    run_length = 0
    for i in range(len(L)) :
        curr_val = L[i]
        curr_length = 1
        curr_sum = curr_val
        increasing = True
        equal = False
        for j in range(i+1, len(L)) :
            if j == i + 1 or equal :
                if L[j] == curr_val :
                    equal = True
                elif L[j] < curr_val :
                    increasing = False
                    equal = False
                else :
                    increasing = True
                    equal = False
            if equal :
                curr_length += 1
                curr_sum += L[j]
                curr_val = L[j]
            elif increasing :
                if L[j] >= curr_val :
                    curr_length += 1
                    curr_sum += L[j]
                    curr_val = L[j]
                else :
                    if curr_length > run_length :
                        run_sum = curr_sum
                        run_length = curr_length
                    break
            else :
                if L[j] <= curr_val :
                    curr_length += 1
                    curr_sum += L[j]
                    curr_val = L[j]
                else :
                    if curr_length > run_length :
                        run_sum = curr_sum
                        run_length = curr_length
                    break
        if curr_length > run_length :
            run_sum = curr_sum
            run_length = curr_length
    return run_sum

# testing
# L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
# L = [5, 4, 10]
# L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# L = [1, 2, 1, 2, 1, 2, 1, 2, 1]
# L = [1, 2, 3, 4, 5, 0, 10, 1, 2, 3, 4, 5]
# L = [1, 2, 3, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# L = [100, 200, 300, 400, 0, 10000, 20000]
# L = [3, 3, 3, 3, 3, 3, 3, -10, 1, 2, 3, 4]
# L = [1, 2, 3, 2, 1, -10, -20, 3, 3, 3, 3, 3, 3, 3, 3, 3]
# L = [1, 2, 3, 2, 1, -10, -20, 3, 4, 5, 7, 7, 8, 9, 11, 11]
# L = [100000, 10000, 1000, 100, 10, 8, 8, 5, 2, 1, 0]
# L = [1, 2, 3, 2, 1, 10, 100, 50, 20, 1000, 10000, 5000, 2000, 100000, 200000, 150000, 100000]
# L = [100000, 150000, 200000, 100000, 2000, 5000, 10000, 1000, 20, 50, 100, 10, 1, 2, 3, 2, 1]
# L = [100, 10, 10, 10, 10, 10, 10, 10, 0]
# L = [-1, -10, -10, -10, -10, -10, -10, -100]
L = [1, 2, 1, 2, 1, 2, 1, 2, -1, -2, -1, -2, 10, 20, 10, 20, 100, 200, 100, 0, 100, 0, 100, 0, 0, 100, 0, 0, 0, 100, 1500000, -1500000, 1, -150001]
print(longest_run(L))