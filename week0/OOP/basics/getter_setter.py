
#he @property decorator. It allows you to treat a method like an attribute.
class Employee:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        # This acts as the GETTER
        return self.__name

    @name.setter
    def name(self, new_name):
        # This acts as the SETTER
        if len(new_name) > 2:
            self.__name = new_name
        else:
            raise ValueError("Name too short!")

emp = Employee("Bob")

# No parentheses! Treat it like a variable.
print(emp.name)      # Bob
emp.name = "Alice"   # Runs the setter
print(emp.name)      # Alice
# emp.name = "Al"    # ValueError: Name too short!
