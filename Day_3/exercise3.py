# Nested if in first exercise
# ask the users height and age, then print if they are eligible to  ride and how much their ticket cost

# height should be more than 120cms 
# if older than 18 ticket is $12, if less than 18 then ticket is $7 

print("Welcome to te rollercoaster")

height = int(input("Enter your Height (in CMs): "))
age = int(input("Enter your age: "))

if height >= 120:
    if age < 12:
        print("Yay, you are good to ride, please pay $5 fot the ticket")
    elif age >= 12 and age < 18:
        print("Yay, you are good to ride, please pay $7 for the ticket")
    else:
        print("Yay, you are good to ride, please pay $12 for the ticket")
else:
    print("!Sorry!, you are not tall enough to ride this ride")
