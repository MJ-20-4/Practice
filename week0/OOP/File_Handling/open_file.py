# Reading from a file in Python
with open("data.txt", "r") as file:
    content = file.read()     #reads the entire content of file
    print(content)              

with open("data.txt", "r") as file:
    print(file.readline())  # First line
    print(file.readline())  # Second line

with open("data.txt", "r") as file:
    lines = file.readlines()
    print(lines)  # ['Line 1\n', 'Line 2\n', 'Line 3\n'] reads all lines into a list

with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # .strip() removes the \n at the end
