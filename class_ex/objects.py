from math import hypot


class Point:

    """
    point in 2D
    >>> p1 = Point(3,4)
    >>> p2 = Point(0,0)
    >>> dis = p1.distance(p2) -> 5
    """

    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def distance(self, other: "Point") -> float:
        return hypot(self.x-other.x, self.y-other.y)


p1 = Point(3, 6)


p2 = Point()
p2.x = 44
p2.y = "sdf"


print(p1.x)
print(p1.y)

p1.reset()
print(p1.x)
print(p1.y)

p2.move(67, 8)
print(p2.x)
print(p2.y)

a = p2.distance(p2)
print(a)


print(help(Point))
print(Point.__doc__)
