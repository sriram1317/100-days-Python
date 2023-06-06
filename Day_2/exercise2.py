# Write a program that calculates BMI from user's weight and height

#BMI = weight(kg)/height square(m)^2

#result should be converted to whole number 

print('Welcome to BMI calculator')

weight = int(input("Enter your weight in KGs: "))
height = float(input("Enter your height in Meters: "))

BMI = int(weight / (height ** 2))

print(BMI)