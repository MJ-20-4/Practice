import csv

# Writing to a CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "CGPA"])
    writer.writerow(["Alice", 22, 8.5])
    writer.writerow(["Bob", 21, 7.2])

# Reading from a CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Output:
# ['Name', 'Age', 'CGPA']
# ['Alice', '22', '8.5']
# ['Bob', '21', '7.2']
