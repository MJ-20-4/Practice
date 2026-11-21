def add(a, b):
    return a+b

def is_even(n):
    return n % 2 ==0

def is_odd(n):
    return n % 2!= 0

def facto(n):
    if n==0:
        return 1
    else:
        return n*facto(n-1)  #recursion

def factorial(n):
    if n < 0:
        return "Invalid"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")

def is_palindrome(s):
    return s == s[::-1]


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

def calculator(a, op, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"



print(f"add(10, 5)              -> {add(10, 5)}")
print(f"is_even(4)              -> {is_even(4)}")
print(f"is_odd(7)               -> {is_odd(7)}")
print(f"facto(5)                -> {facto(5)}")
print(f"factorial(5)            -> {factorial(5)}")
print(f"count_vowels('Maahi')   -> {count_vowels('Maahi')}")
print(f"is_palindrome('madam')  -> {is_palindrome('madam')}")

print("fib(7)                  -> ", end="")
fib(7)  # This prints inside the function
print(f"\ncalculator(10, '+', 5)  -> {calculator(10, '+', 5)}")
print(f"calculator(10, '/', 0)  -> {calculator(10, '/', 0)}")
