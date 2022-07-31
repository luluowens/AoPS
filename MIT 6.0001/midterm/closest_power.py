def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    while base ** exp <= num :
        if base ** exp == num :
            return exp
        if base ** (exp + 1) <= num :
            exp += 1
        else :
            if num - base ** exp <= base ** (exp + 1) - num :
                return exp
            else :
                return exp + 1



import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        self.assertEqual(closest_power(3, 12), 2)
        self.assertEqual(closest_power(4, 12), 2)
        self.assertEqual(closest_power(4, 1), 0)
        

if __name__ == '__main__':
    unittest.main()