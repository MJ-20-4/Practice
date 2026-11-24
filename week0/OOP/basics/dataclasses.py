from dataclasses import dataclass

'''
Writing __init__, __str__, and __eq__ for every class is repetitive. 
Python 3.7 introduced @dataclass to generate all this boilerplate code automatically!
'''



@dataclass
class Point:
    x: int
    y: int
    z: int = 0  # Default value

p1 = Point(1, 2, 3)
p2 = Point(1, 2, 3)

print(p1)          # Point(x=1, y=2, z=3)  (__str__ generated)
print(p1 == p2)    # True                   (__eq__ generated)
