''' PYTHON DATA TYPES - COMPLETE DEMO PROGRAM

---------- 1. INTEGER ----------'''

age = 22
count = -50
big_number = 1_000_000
print("INTEGER:")
print(type(age), type(count), type(big_number), "\n")

# ---------- 2. FLOAT ----------
cgpa = 7.14
pi = 3.14159
temperature = -2.5
print("FLOAT:")
print(type(cgpa), type(pi), type(temperature), "\n")

# ---------- 3. COMPLEX ----------
z = 3 + 4j
print("COMPLEX:")
print(type(z), "\n")

# ---------- 4. STRING ----------
name = "Maahi"
city = 'Mumbai'
message = """Hello, this is
a multi-line string"""
print("STRING:")
print(type(name), type(city), type(message), "\n")

# ---------- 5. BOOLEAN ----------
isstudent = True
is_married = False
print("BOOLEAN:")
print(type(isstudent), type(is_married), "\n")

# ---------- 6. LIST ----------
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]
print("LIST:")
print(type(fruits), type(numbers), type(mixed), "\n")

# ---------- 7. TUPLE ----------
coordinates = (10, 20)
single_tuple = (5,)
print("TUPLE:")
print(type(coordinates), type(single_tuple), "\n")

# ---------- 8. RANGE ----------
my_range = range(1, 6)
print("RANGE:")
print(type(my_range), "\n")

# ---------- 9. SET ----------
colors = {"red", "green", "blue", "red"}
unique_nums = {1, 2, 3, 4}
print("SET:")
print(type(colors), type(unique_nums), "\n")

# ---------- 10. FROZENSET ----------
frozen = frozenset([1, 2, 3])
print("FROZENSET:")
print(type(frozen), "\n")

# ---------- 11. DICTIONARY ----------
person = {"name": "Maahi", "age": 22, "cgpa": 7.14}
marks = {"math": 95, "science": 88}
print("DICTIONARY:")
print(type(person), type(marks), "\n")

# ---------- 12. BYTES ----------
byte_data = b"hello"
print("BYTES:")
print(type(byte_data), "\n")

# ---------- 13. BYTEARRAY ----------
byte_arr = bytearray(b"abc")
print("BYTEARRAY:")
print(type(byte_arr), "\n")

# ---------- 14. MEMORYVIEW ----------
mem_view = memoryview(b"abc")
print("MEMORYVIEW:")
print(type(mem_view), "\n")

# ---------- 15. NONE TYPE ----------
result = None
print("NONE TYPE:")
print(type(result), "\n")

