# upgraded BMI calculator

print("Welcome to BMI calculator")

height = float(input("Enter your height in Meter: "))
weight = float(input("Enter your weight in Kg: "))


bmi = round(weight / (height ** 2), 2)

print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
elif bmi >= 30 and bmi < 35:
    print("Obese")
elif bmi > 35:
    print("Clinically Obese")