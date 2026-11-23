#inheritance
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Woof!")

d = Dog()
d.eat()   # Inherited from Animal
d.bark()  # Defined in Dog


#encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Double underscore makes it PRIVATE we use _ (protected) and __ (private) prefixes.

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance()) # 1500

# print(acc.__balance)   # ❌ AttributeError (Cannot access from outside)


#polymorphism

class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Woof")

# Same method name, different behavior
for animal in [Cat(), Dog()]:
    animal.sound()
# Meow
# Woof

