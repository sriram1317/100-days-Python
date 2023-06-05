# Project to generate a band name

# Steps: 1 - greet the user
#   2 - Ask the city they are born/grew up
#   3 - Ask for name of pet
#   4 - Combine name of city and pet and show their band name
#   5 - Make sure input cursor is on new line


# Step 1: Greet
print("Hi! good day. Welcome to band name generator")

# Step 2: City name
cityName = input("what's the name of city you grew up on? \n")

# Step 2: Pet name
petName = input("what's the name of your pet? \n")


# Step 3: combine the names
bandName = cityName + ' ' + petName

print("Your Band name can be: " + bandName)
