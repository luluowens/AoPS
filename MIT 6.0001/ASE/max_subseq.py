def max_contig_subseq_sum(L):
    """ 
    L is a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L. A contiguous subsequence
    is made up of consecutive elements. It can be of any length, and start at any point. 
    """
    max_sum = L[0]
    for i in range(len(L)) :
        curr_sum = 0
        for j in range(i, len(L)) :
            curr_sum += L[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum
    


# testing
print(max_contig_subseq_sum([3, 4, -1, 5, -4]))   # prints 11
print(max_contig_subseq_sum([3, 4, -8, 15, -1, 2]))  # prints 16  
print(max_contig_subseq_sum([-10, -11, 12, -13, 0]))  # prints 12
print(max_contig_subseq_sum([10, -9, 35, -13, 0]))  # prints 36