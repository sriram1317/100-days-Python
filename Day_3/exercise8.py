# program to find compatibility between two people


print("Welcome to love calculator")

name1 = input("Enter first name\n")
name2 = input("Enter second name\n")

name = name1 + name2
name = name.lower()

t = name.count('t')
r = name.count('r')
u = name.count('u')
e = name.count('e')
l = name.count('l')
o = name.count('o')
v = name.count('v')
e = name.count('e')

true = t + r + u + e
love = l + o + v + e

score = str(true) + str(love)
num = int(score)

if num <= 10 or num >= 90:
    print(f"Your score is {num}, you go togeter like coke and mentos")
elif num >= 40 and num <= 50:
    print(f"Your score is {num}, you are alright together")
else:
    print(f"Your score is {num}")