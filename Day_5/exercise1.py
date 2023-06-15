# Average height of students from the list of students

studentList = input("Input the list of students:\n").split()
sum = 0
l = len(studentList)

for student in studentList:
    sum += int(student)

avg = int(round(sum / l, 2))

print(f"Average height is {avg}")