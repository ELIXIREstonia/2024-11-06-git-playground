class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point(%s, %s)" % (self.x, self.y)
    
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    
class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def __str__(self):
        return "Circle(%s, %s)" % (self.center, self.radius)
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return "Triangle(%s, %s, %s)" % (self.a, self.b, self.c)
    
    def area(self):
        s = (self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)) / 2
        return (s * (s - self.a.distance(self.b)) * (s - self.b.distance(self.c)) * (s - self.c.distance(self.a))) ** 0.5
    
    def perimeter(self):
        return self.a.distance(self.b) + self.b.distance(self.c) + self.c.distance(self.a)
    
p1 = Point(0, 0)
p2 = Point(3, 4)
print(f"The distance between {p1} and {p2} is {p1.distance(p2)}")
c = Circle(p1, 5)
print(f"The area of {c} is {c.area():.2f}")
t = Triangle(p1, p2, Point(0, 3))
print(f"The area of {t} is {t.area():.2f}")
print(f"The perimeter of {t} is {t.perimeter():.2f}")