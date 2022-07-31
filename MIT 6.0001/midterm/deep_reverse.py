def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for i in range(len(L)) :
        for j in range(len(L[i])//2) :
            L[i][j], L[i][len(L[i]) - j - 1] = L[i][len(L[i]) - j - 1], L[i][j]

    for i in range(len(L)//2) :
        L[i], L[len(L) - i - 1] = L[len(L) - i - 1], L[i]
 

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
# L = [[1, 2], [3, 4], [5, 6, 7]]
deep_reverse(L) 
print(L)


# import unittest

# class TestLinkedList(unittest.TestCase) :

#     def test_solution(self) :
#         self.assertEqual(deep_reverse([[1, 2], [3, 4], [5, 6, 7]]), [[7, 6, 5], [4, 3], [2, 1]])
#         # self.assertEqual(deep_reverse([1,0,1], [1,0,-1]), 0)
        

# if __name__ == '__main__':
#     unittest.main()
