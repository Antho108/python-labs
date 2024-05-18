# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.


# user = int(input("Enter a numberbetween 0 and 1,000,000,000."))
# num = None

# while num != user:
#     num = True
#     print(num)
#     break
# print(user)


user = int(input("Enter a number between 0 and 1,000,000,000: "))
num = None

while num != user:
    num = int(input("Guess the number: "))

print("Congratulations! You found the number:", num)




 

    