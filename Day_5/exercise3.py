# Add even numbers from 1 to 100 (inclusive)

sum = 0

# for num in range(1,101):
#     if num % 2 == 0:
#         sum += num
#         print(num)

for num in range(2,101,2):
    sum += num

print(f"Sum of even numbers between 1 - 100 is {sum}")