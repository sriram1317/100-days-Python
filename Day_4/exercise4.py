# Rock paper scissor
import random

plCh = int(input("What do you choose? 1 for Rock, 2 for Paper and 3 for Scissors: "))
pcCh = random.randint(0,2) + 1

scissor = "Scissor"
paper = "Paper"
rock = "Rock"

if plCh == 1:
    plCho = rock
elif plCh == 2:
    plCho = paper
elif plCh == 3:
    plCho = scissor

if pcCh == 1:
    pcCho = rock
elif pcCh == 2:
    pcCho = paper
elif pcCh == 3:
    pcCho = scissor

print(f"Player chose: {plCho}")
print(f"Computer chose: {pcCho}")

if plCh == pcCh:
    print("!Its a Draw")

else:
    if plCh == 1:
        if pcCh == 2:
            print("!You lose")
        else:
            print("!You won!")
    elif plCh == 2:
        if pcCh == 3:
            print("!You lose")
        else:
            print("!You won!")
    elif plCh == 3:
        if pcCh == 1:
            print("!You lose")
        else:
            print("!You won!")

