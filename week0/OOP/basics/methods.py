#class method
"""Methods that work on the class itself, not the instance.
 They take cls instead of self.
"""

class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, name_str):
        return cls(name_str.capitalize())

p = Person.from_string("maahi")
print(p.name) # Maahi

#static method
'''Methods that don't need access to self or cls. 
They are just normal functions grouped inside a class for logical organization
'''
class Math:
    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(5, 5)) # 10
