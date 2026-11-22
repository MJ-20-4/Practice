class Car:
    pass

# Creating objects (instances)
my_car = Car()
your_car = Car()

print(type(my_car))  # <class '__main__.Car'>

class Car:
    # The __init__ method runs automatically when you create a new object
    def __init__(self, brand, color):
        self.brand = brand  # Attribute
        self.color = color  # Attribute

car1 = Car("Toyota", "Red")
print(car1.brand)  # Toyota
print(car1.color)  # Red

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        print(f"{self.brand} is driving!")

car1 = Car("Toyota")
car1.drive()  # Toyota is driving!
