# Given two integer numbers return 
# their product only if the product is equal to or lower than 1000, else return their sum.

# number1 = 20
# number2 = 30
# sum = number1 + number2 
# pro = number1 * number2


# if pro == 1000 or pro < 1000: 
#     print(pro)
# else: 
#     print(sum)


# number1 = 40
# number2 = 30
# pro = number1 * number2 
# sum = number1 + number2


# if pro == 1000 or pro < 1000: 
#     print(pro) 
# else:
#     print(sum)


# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

# previous_num = 0

# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("current number", i,  "previous number", previous_num, "total", x_sum)
#     previous_num = i


# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.


# accept input string from a user
# word = input('Enter word ')
# print("Original String:", word)

# # get the length of a string
# size = len(word)

# # iterate a each character of a string
# # start: 0 to start with first character
# # stop: size-1 because index starts with 0
# # step: 2 to get the characters present at even index like 0, 2, 4
# print("Printing only even index chars")
# for i in range(0, size - 1, 2):
#     print("index[", i, "]", word[i])


# **************************************************************************

# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

# For example:

# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.



for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )