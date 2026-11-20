
name =input("name ")
age= int(input("age "))
a,b,c=input("enter 3 nosby spaces ").split() #Strings
print(name,age,a,b,c) 
e,f,g=map(int,input("enter 3 nos by space ").split()) #Integers
print(e+f+g)
#Read list of Nos Type of Items Inside
numbers=list(map(int,input("enter list of nos by spaces ").split()))
print(numbers)

numbers=list(input("enter list of nos by commas ").split(","))
print(type(numbers))
words = input("Enter as many words as you want: ").split()
print(type(words))
# int(input()) fails if user types text
n = int(input("Number: "))     # user types "abc" → ValueError

# FIX: use try/except
while True:
    try:
        n = int(input("Number: "))
        break
    except ValueError:
        print("Not a valid number!")

#  Forgetting input() returns str
age = input("Age: ")           # "22"
print(age + 1)                 #  TypeError

#  Extra spaces
name = input("Name: ")         # " Maahi "
name = name.strip()            # "Maahi" (cleans it)


def add(a, b):
    """Return the sum of a and b."""   #  docstring — stored in __doc__ top of file, but after an import 
    '''A docstring is a string literal that appears as the very first statement inside:

    a module (top of .py file)

    a function

    a class

    a method '''
    return a + b

print(add.__doc__)   # "Return the sum of a and b."
