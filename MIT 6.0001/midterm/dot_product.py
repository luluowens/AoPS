'''Write a Python function that returns the sum of the pairwise products of listA and listB.
You should assume that listA and listB have the same length and are two lists of integer
numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is
1*4 + 2*5 + 3*6, meaning your function should return: 32
'''

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dot_product = 0
    for i in range(len(listA)) :
        dot_product += listA[i] * listB[i]
    return dot_product


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        self.assertEqual(dotProduct([1,2,3], [4,5,6]), 32)
        self.assertEqual(dotProduct([1,0,1], [1,0,-1]), 0)
        

if __name__ == '__main__':
    unittest.main()