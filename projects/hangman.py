# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script

# Print an explanation to the user

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# // Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it
#  look function enumerate


attemps = 0 
word_final = "Faridabad"
user_input = None 

print(" Welcome to my special Hangman games") # Welcome message 
user_name = input("Enter your name ")

print(f" You have only 5 attemps to find the good names, enter only one character, good luck {user_name} ") # Print an explanation to the user

print("_________")

while user_input != "Faridabad ": 
    user_input = input("Find the correct character and display the name. \n")[0]
    attemps += 1
    print(user_input[0])
    if user_input == word_final : 
        print("You win, you are a champion ")
        exit()
print(user_input[0])



# x = ('apple', 'banane', 'popo')
# y = enumerate(x)

# print(list(y))
