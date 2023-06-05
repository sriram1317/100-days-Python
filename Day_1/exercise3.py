# Exercise: Write a program that switches int values stored in variables a and b without using another variable

a = int(input("Provide value for a: "))
b = int(input("Provide value for b: "))

a = a + b
b = a - b
a = a - b

print("Value of a: " + str(a))
print("Value of b: " + str(b))
