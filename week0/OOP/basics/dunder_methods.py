'''Dunder means Double Underscore.
 These allow you to customize how your objects 
 behave with built-in Python operators 
 (+, ==, len(), print()).
 __init__ : Constructor

__str__ : Used by print() and str()

__repr__ : Used by the console/debugging

__len__ : Used by len()

__eq__ : Used by ==

__add__ : Used by +
 
 '''



class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    # 1. String representation (for print)
    def __str__(self):
        return f"Book: {self.title}"

    # 2. Length (for len())
    def __len__(self):
        return self.pages

    # 3. Addition (for +)
    def __add__(self, other):
        return self.pages + other.pages

b1 = Book("Python 101", 300)
b2 = Book("OOP Guide", 200)

print(b1)          # Book: Python 101
print(len(b1))     # 300
print(b1 + b2)     # 500 (adds pages)
