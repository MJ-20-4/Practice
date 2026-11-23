class Employee:
    company = "TechCorp"  # Class Attribute (Shared)

    def __init__(self, name):
        self.name = name  # Instance Attribute (Unique)

emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(emp1.company) # TechCorp
print(emp2.company) # TechCorp
