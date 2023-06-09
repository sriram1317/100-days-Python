# adding more conditions in exerise 3

# Nested if in first exercise
# ask the users height and age, then print if they are eligible to  ride and how much their ticket cost

# height should be more than 120cms 
# if older than 18 ticket is $12, if less than 18 then ticket is $7 
# ask if a photo needs to be taken add the amount int the ticket 

print("Welcome to te rollercoaster")

height = int(input("Enter your Height (in CMs): "))
age = int(input("Enter your age: "))
bill = 0
photo = ''
ride = ''

if height >= 120:
    if age < 12:
        ride = 'Y'
        bill += 5
    elif age >= 12 and age < 18:
        ride = 'Y'
        bill += 7
    else:
        ride = 'Y'
        bill += 12
    photo = input("Want your photo taken during the ride (Y/N)")
    photo = photo.upper()
    if photo == 'Y':
        bill += 3
else:
    ride = 'N'

if ride == 'Y':
    print(f"Yay, you are good to ride, please pay ${bill} for the ticket")
elif ride == 'N':
    print("Sorry! you are tall enough for the ride")