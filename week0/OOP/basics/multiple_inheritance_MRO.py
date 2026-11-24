class Flyer:
    def fly(self): print("Flying")

class Swimmer:
    def swim(self): print("Swimming")

class Duck(Flyer, Swimmer):  # Inherits from both
    pass

d = Duck()
d.fly()   # Flying
d.swim()  # Swimming

#The super() Function Used to call a method from the parent class (usually __init__).
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls Animal's __init__ (sets self.name)
        self.breed = breed      # Sets Dog's specific attribute

d = Dog("Buddy", "Labrador")
print(d.name, d.breed) # Buddy Labrador
