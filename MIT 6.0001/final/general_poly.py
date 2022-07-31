def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def func(x) :
        k = len(L)
        poly_ans = 0
        for i in range(k) :
            poly_ans += L[i] * (x ** (k - i - 1))
        return poly_ans
    return func

print(general_poly([1, 2, 3, 4])(10))