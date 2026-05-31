import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
        
        
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def distance (self, value):
        return math.sqrt((self.x - value.x)**2 + (self.y - value.y)**2)
    
class Vector(Point):
        def __init__(self, x, y):
             super().__init__(x, y)
        
        def __str__(self):
             return f'Vector ({self.x} : {self.y})'
        
        def __add__(self,value):
             if not isinstance(value, Point):
                  return False
             return Vector(self.x + value.x, self.y + value.y)



p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(4, 6)

print("p1:", p1)
print("p3:", p3)

print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)

print("distance p1 -> p3:", p1.distance(p3))

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print("v1:", v1)
print("v2:", v2)

v3 = v1 + v2
print("v1 + v2 =", v3)