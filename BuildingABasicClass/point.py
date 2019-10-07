class Point:
    """Represents a point in 2 dimensional space"""

    default_x = 0
    default_y = 0

    @staticmethod
    def distance(p1, p2):
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** .5

    @classmethod
    def from_tuple(cls, coords):
        return cls(coords[0], coords[1])

    def __init__(self, x=default_x, y=default_y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __sub__(self, other):
        return Point.distance(self, other)

Point # <--- this is a class
p1 = Point(1, 25) # <--- this is an object
p1.x = 5

p2 = Point.from_tuple((2, 35))

p1 - p2


class ValuePoint(Point):

    def __init__(self, x, y, value=None):
        super().__init__(x, y)
        self.value = value

    def __str__(self):
        return f'ValuePoint({self.x}, {self.y}, {self.value})'

p3 = ValuePoint(5, 5, 5)
print(p1 - p3)
