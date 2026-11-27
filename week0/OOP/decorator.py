#They use Higher-Order Functions (functions that take other functions as arguments).
'''A decorator is a function that wraps around another function 
to add extra behavior without modifying the original function's code.
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening BEFORE the function is called.")
        func()
        print("Something is happening AFTER the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
