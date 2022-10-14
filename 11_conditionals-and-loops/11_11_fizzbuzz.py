# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

x = int(input("Enter your number"))


if x%5 and x%3 == 0:
    print("FlizzBuzz")
elif x%3 == 0:
    print("Fizz")
elif x%5 == 0: 
    print("Buzz")
else:
     print(x)