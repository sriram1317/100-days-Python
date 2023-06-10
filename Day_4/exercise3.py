# Edit a 2D list

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]
map = [row1,row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

pos = input("Where do you want to put the treasure box? ")

i = int(pos[0]) - 1
j = int(pos[2]) - 1

map[j][i] = "X"

print(f"{map[0]}\n{map[1]}\n{map[2]}\n")