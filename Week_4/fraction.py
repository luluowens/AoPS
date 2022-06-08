'''Write a new class $\verb#Fraction#$ to represent fractions, like 2/3.

A Fraction should have two attributes num and denom to represent the numerator and denominator.
Each should be an integer, and the denominator cannot be 0.
Your code should not let users create a fraction with denominator equal to zero.
Since we haven't talked about how to make a class refuse to create an object,
we've got you started in the code below with two lines in the __init__ method
that will deal with that case by $raising$ a division-by-zero error message.

The string representation method should return a string representing the fraction 
in lowest terms and always with a positive denominator. (See examples below.)

Also write a floating-point representation special method __float__
that returns the float that's equal to the fraction. (See examples below.)

Additionally, write methods to add, subtract, multiply, and divide fractions.
Each of these should take two arguments (self and other) and return a Fraction object.
(See examples below.)

Finally, write a method to test if two fractions are equal. It should return a boolean:
True if they are equal, and False if not.

If you like, you may overload the regular arithmetic operators for all of these using
the special methods __add__, __sub__, __mul__, __truediv__, and __eq__.
Because __truediv__ does not work in the widget, you should do your testing in Python IDLE.
Or, you can write these operators as "ordinary" methods such as add(), sub(), and so on.
'''

import math

class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError()
        self.num = num
        self.denom = denom

    def simplify(self) :
        gcd = math.gcd(self.num, self.denom)
        self.num = int(self.num / gcd)
        self.denom = int(self.denom / gcd)
        if self.denom < 0 :
            self.num = -1 * self.num
            self.denom = -1 * self.denom

    def __str__(self) :
        '''returns a string when looking for fraction
        '''
        self.simplify()
        return f'{self.num}/{self.denom}'

    def __float__(self) :
        return float(self.num / self.denom)

    def add(self, other) :
        num = self.num * other.denom + self.denom * other.num
        denom = self.denom * other.denom
        sum_fracs = Fraction(num, denom)
        sum_fracs.simplify()
        return sum_fracs

    def sub(self, other) :
        num = self.num * other.denom - self.denom * other.num
        denom = self.denom * other.denom
        sub_fracs = Fraction(num, denom)
        sub_fracs.simplify()
        return sub_fracs

    def mul(self, other) :
        num = self.num * other.num
        denom = self.denom * other.denom
        mul_fracs = Fraction(num, denom)
        mul_fracs.simplify()
        return mul_fracs

    def div(self, other) :
        num = self.num * other.denom
        denom = self.denom * other.num
        div_fracs = Fraction(num, denom)
        div_fracs.simplify()
        return div_fracs

    def eq(self, other) :
        self.simplify()
        other.simplify()
        return self.num == other.num and self.denom == other.denom

# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if implementing "normal" arithmetic methods
print(p.add(q))       # should print 1/3, since 1/2 + (-1/6) = 1/3
print(p.sub(q))  # should print 2/3, since 1/2 - (-1/6) = 2/3
print(p.sub(p))  # should print 0/1, since p-p is 0
print(p.mul(q)) # should print -1/12
print(p.div(q))  # should print -3/1
print(p.eq(r))   # should print True
print(p.eq(q))   # should print False
### if overloading using special methods
# print(p+q)  # should print 1/3
# print(p-q)  # should print 2/3
# print(p-p)  # should print 0/1
# print(p*q)  # should print -1/12
# print(p/q)  # should print -3/1
# print(p==r) # should print True
# print(p==q) # should print False