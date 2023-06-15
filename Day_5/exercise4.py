# FizzBuzz

# Program shoul print each number from 1 - 100
# When a number is divisible by 3, then instead of printing number print "Fizz"
# When a number is divisible by 5, then instead of printing number print "Bizz"
# When a number is divisible by 3 and 5, then instead of printing number print "FizzBizz"

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)