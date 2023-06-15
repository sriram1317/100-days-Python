# Highest score in a list of stuent marks

studentMarks = input("INput the list of marks of students:\n").split()
max1 = 0

for mark in studentMarks:
    if int(mark) > max1:
        max1 = int(mark)

# max1 = max(studentMarks)

print(f"The highest marks int the class is {max1}")