#nested loop
for i in range(3):
    for j in range(3):
        print(f"({i},{j})", end=" ")
    print() 

#break and nested loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break       # exits inner only
        print(i, j)

#to break out of both loops,use a flag
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break
print("Found at", i, j)

# Right triangle
n = 5
for i in range(1, n + 1):
    print("*" * i)

print()

# Inverted triangle
for i in range(n, 0, -1):
    print("*" * i)

print()

# Pyramid
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))

print()

# Number pyramid
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print()

# Multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()
