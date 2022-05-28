class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def slope(self, q) :
        if self.x == q.x :
            return "undefined"
        else :
            return abs(self.y - q.y) / abs(self.x - q.x)
    
    def is_on(self, p, q) :
        slope_rp = self.slope(p)
        slope_rq = self.slope(q)
        if isinstance(slope_rp, str) and isinstance(slope_rq, str) :
            if self.x == p.x :
                return True
            else :
                return False
        else :
            if slope_rp == slope_rq :
                return True
            else :
                return False


# # slope test cases
# p = Point(1,-2)
# q = Point(3,5)
# r = Point(3,7)
# print(p.slope(q))  # should be 3.5
# print(q.slope(p))  # should be 3.5
# print(q.slope(r))  # should print "undefined"


# is_on test cases
p = Point(0,0)
q = Point(3,6)
r = Point(1,2)
s = Point(2,3)
print(r.is_on(p,q))   # should be True
print(s.is_on(p,q))   # should be False