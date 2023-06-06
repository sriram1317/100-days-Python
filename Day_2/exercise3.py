# Write a code that prints how many days, months and years we have left in our life if we live till 90 years old.

print("Hey! welcome to your lifespan calculator which calculates yyour remaining lifespan if you live till 90 years old")

curAge = int(input("Enter your current age: "))

yearRem = 90 - curAge
remDays = yearRem * 365
remWeek = yearRem * 52
remMon = yearRem * 12

print(f"You have {remDays} days, {remWeek} weeks and {remMon} months left.")