# Writing to a file in Python
with open("notes.txt", "w") as file:
    file.write("Hello World\n")
    file.write("This is Python.\n")  # overwrites the file if it already exists

with open("notes.txt", "a") as file:
    file.write("Adding a new line.\n")
    file.write("Without deleting the old ones.\n") # appends to the file if it already exists

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("notes.txt", "w") as file:
    file.writelines(lines) #writes a list of lines to the file


#  file.write(42)  -> TypeError: write() argument must be str
with open("data.txt", "w") as file:
    file.write(str(42) + "\n")  # Converts the integer to a string before writing to the file
