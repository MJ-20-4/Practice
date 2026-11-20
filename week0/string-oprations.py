a='sigle'
b="doble"
c="""triple
line """
print(a,b,c)
s4 = str(42)              # "42"
s5 = "abc" * 3            # "abcabcabc"
s6 = "Hello" + " " + "World"   # "Hello World"
print(s4, s5, s6)
s = "Python"

# Indexing (0-based)
s[0]        # 'P'
s[1]        # 'y'
s[-1]       # 'n'  (last)
s[-2]       # 'o'  (second last)

# Slicing  [start:stop:step]
s[0:3]      # 'Pyt'
s[2:]       # 'thon'
s[:3]       # 'Pyt'
s[:]        # 'Python'  (full copy)
s[::2]      # 'Pto'     (every 2nd)
s[::-1]     # 'nohtyP'  (reverse!)
s[-3:]      # 'hon'     (last 3)

#concatenaton & repetition
print("Hello" + " " + "World"  )  # "Hello World"
print("ab" * 3 )                  # "ababab"
print("ab" * 0 )                  # ""
print("-" * 20 )                  # "--------------------"

s = "Hello, World"
#Membership
print("Hello" in s)        # True
print("world" in s)        # False (case-sensitive!)
print("World" in s)        # True
print("xyz" not in s)      # True
print("o" in s)            # True

#length and comparison
print(len("Python"))       # 6
print(len(""))             # 0

print("abc" == "abc")      # True
print("abc" == "ABC")      # False (case-sensitive)
print("abc" < "abd")       # True (lexicographic)
print("Apple" < "apple")   # True (uppercase < lowercase in ASCII)

#case methods
s = "Hello World"

print(s.upper())           # "HELLO WORLD"
print(s.lower())           # "hello world"
print(s.title())           # "Hello World"
print(s.capitalize())      # "Hello world"
print(s.swapcase())        # "hELLO wORLD"
print(s.casefold())        # "hello world"  (aggressive lowercase)

# Check case
print("HELLO".isupper())   # True
print("hello".islower())   # True
print("Hello".istitle())   # True

#whitespaceand strip methods
s = "   Hello   "

print(s.strip())           # "Hello"       (both sides)
print(s.lstrip())          # "Hello   "    (left only)
print(s.rstrip())          # "   Hello"    (right only)

# Custom characters
print("***Hello***".strip("*"))     # "Hello"
print("xxHelloxx".strip("x"))       # "Hello"

#Searching and finding
s = "Hello, World"

print(s.find("World"))         # 7     (first index, -1 if not found)
print(s.rfind("o"))            # 8     (last index)
print(s.index("World"))        # 7     (like find but raises ValueError)
print(s.rindex("o"))           # 8

print(s.count("o"))            # 2     (count occurrences)
print(s.count("l"))            # 3

#check string content
print("abc123".isalnum())      # True   (letters + digits only)
print("abc".isalpha())         # True   (letters only)
print("123".isdigit())         # True   (digits only)
print("123".isnumeric())       # True   (unicode numerics)
print("abc".isidentifier())    # True   (valid Python name)
print("   ".isspace())         # True   (whitespace only)

print("HELLO".isupper())       # True
print("hello".islower())       # True
print("Hello World".istitle()) # True

#split and join
print("a,b,c".split(","))          # ['a', 'b', 'c']
print("a b c".split())             # ['a', 'b', 'c']  (whitespace)
print("a b c".split(" "))          # ['a', 'b', 'c']
print("a-b-c".split("-"))          # ['a', 'b', 'c']
print("a-b-c".split("-", 1))       # ['a', 'b-c']  (max 1 split)
print("hello".split("l"))          # ['he', '', 'o']
print("".split(","))               # ['']

print(",".join(["a", "b", "c"]))      # "a,b,c"
print("-".join(["2026", "11", "20"]))  # "2026-11-20"
print(" ".join(["Hello", "World"]))    # "Hello World"
print("".join(["a", "b", "c"]))        # "abc"
print("\n".join(["line1", "line2"]))   # "line1\nline2"

#replace
print("Hello".replace("l", "L"))         # "HeLLo"
print("a-b-c".replace("-", "_"))           # "a_b_c"
print("aaa".replace("a", "b"))             # "bbb"
print("aaa".replace("a", "b", 2))          # "bba"  (max 2 replacements)
print("Hello".replace("xyz", "abc"))       # "Hello"  (no match → unchanged)

#startswith and endswith
s = "hello.py"

print(s.startswith("hello"))       # True
print(s.startswith("HELLO"))       # False (case-sensitive)
print(s.startswith(("hi", "hello")))  # True (any of tuple)

print(s.endswith(".py"))           # True
print(s.endswith((".py", ".txt"))) # True (any of tuple)

#formatting methods
name = "Maahi"
age = 22
cgpa = 7.14159

f"{name} is {age}"                  # "Maahi is 22"
f"{cgpa:.2f}"                       # "7.14"
f"{cgpa:10.2f}"                     # "      7.14"
f"{age:03d}"                        # "022"
f"{age:>5}"                         # "   22"
f"{age:<5}"                         # "22   "
f"{age:^5}"                         # " 22  "
f"{255:x}"                          # "ff"  (hex)
f"{255:b}"                          # "11111111"  (binary)
f"{0.75:.0%}"                       # "75%"

#alignment &padding
print("hi".center(10))        # "    hi    "
print("hi".ljust(10))          # "hi        "
print("hi".rjust(10))          # "        hi"
print("hi".zfill(5))           # "000hi"  (zeros left)

print("42".zfill(5))           # "00042"
print("-42".zfill(5))          # "-0042"


#looping through strings 
s = "abc"

# Simple loop
for ch in s:
    print(ch)           # a, b, c

# With index
for i, ch in enumerate(s):
    print(i, ch)        # 0 a, 1 b, 2 c

# Reverse
for ch in reversed(s):
    print(ch)           # c, b, a

#encoding and decoding...
'''Encoding converts data into a standard format
 for safe storage or transmission. 
 Decoding reverses that process back to the original form'''

print("hello".encode())            # b'hello'  (UTF-8 default)
print("hello".encode("utf-8"))     # b'hello'
print("hello".encode("ascii"))     # b'hello'

print(b"hello".decode())           # "hello"
print(b"hello".decode("utf-8"))    # "hello"

print("café".encode("utf-8"))      # b'caf\xc3\xa9'

#reverse a string
s = "hello"
print(s[::-1])                     # "olleh"
s = "madam"
print(s == s[::-1])                # True
s = "hello world"
print(sum(1 for ch in s.lower() if ch in "aeiou"))   # 3

#turncate long string
s = "This is a very long string"
print(s[:10] + "...")              # "This is a ..."
