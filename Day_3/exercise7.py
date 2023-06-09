# Program for ordering pizza with different size and toppings

print("Welcome to ABC pizza deliveries")

size = input("What size pizza do you want? S, M or L: ")
addPepperoni = input("want to add pepporonis? Y or N ")
extraCheese = input("Do you want some extra cheese? Y or N: ")
bill = 0

size = size.upper()
addPepperoni = addPepperoni.upper()
extraCheese = extraCheese.upper()

if extraCheese == 'Y':
    bill += 1

if addPepperoni == 'Y' and size == 'S':
    bill += 2
elif addPepperoni == 'Y' and (size == 'M' or size == 'L'):
    bill += 3

if size == 'S':
    bill += 15
    print(f"Your final bill is ${bill}")
elif size == 'M':
    bill += 20   
    print(f"Your final bill is ${bill}")
elif size == 'L':
    bill += 25
    print(f"Your final bill is ${bill}")
else:
    print("Invalid size selected")
    





