# Write a program to calculate the amount of paint required to paint a wall given the wall's Height and width

# number of cans will be (height of wall times width of wall) divided by average coverage by a can of paint
#since we can't buy the can in fractions, round up to ceil value
import math

def calcNumOfCans(height, width, coverage):
    ans = math.ceil((height * width) / coverage)
    return ans    

height = int(input("Enter the height of wall: "))
width = int(input("Enter the width of wall: "))
coverage = 5

numOfCans = calcNumOfCans(height,width,coverage)

print(f"It woruld take {numOfCans} cans to paint the wall of given height and width.")