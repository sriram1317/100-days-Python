# Who's paying

# write a program to select random name from list of names
import random


names = input("Give me everyone's names, seperated by commas\n")
name = names.split(", ")

l = len(name) - 1

ind = random.randint(0,l)

print(f"{name[ind]} is going to buy everyone's meals")