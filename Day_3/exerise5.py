# Check if the given year is leap year or not

year = int(input("Enter the year to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")        
        else:
            print(f"{year} is a non leap year")
    else:
            print(f"{year} is a leap year")
else:
    print(f"{year} is a non leap year")




# Alternate soluiton

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is a non leap year")