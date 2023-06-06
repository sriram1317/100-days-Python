# write a program that adds two digit numbers. e.g if the input is 35 then the output should be 3 + 5 = 8

num = int(input("Enter a two digit number: "))
sum = 0

while num > 0:
    r = num % 10
    sum += r
    num = int(num / 10)

print(sum)
