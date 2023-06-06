#Tip calculator based on number of people and percentage of tip for each person the bill is being shared with

print("Welcome to the tip calculator")

bill = float(input("What is the total bill amount?: $"))
tipPer = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
numOfPer = int(input("How many people to split the bill with?: "))
payAmt = 0

tipAmt = bill * (tipPer / 100)
totAmt = bill + tipAmt
payAmt = round(totAmt / numOfPer, 2)


print(f"Each person shoul pay: ${payAmt}")