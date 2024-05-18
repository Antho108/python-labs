# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined solution.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a solution that needs to be guessed in the script

# Print an explanation to the user

# Display the solution as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"

# // Ask for user input

# Allow only single-character alphabetic input

# Create a counter for how many tries a user has

# Keep asking them for their guess until they won or lost

# When they find a correct character, display the blank with the solution
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"

# Display a winning message and the full solution if they win

# Display a losing message and quit the game if they don't make it
#  look function enumerate

# Welcome message 
print(" Welcome to my special Hangman games ")

# Player's name
user_name = input("Display your name ")

# Implant the rules and showing then
rules = "Try to guess a name. You have only 7 attempts."
print(rules, "Good luck", user_name)

solution = "God" # Final word to find
attempts = 7 # Declaration variable of attempts number
guess = ""
screen = ""



# Displaying screen with the "_" but i don't know how to add a letter her
for char in solution : 
    screen = screen + "_"
print(screen)


# I want to write here a programm then to check if the letter is inside my solution. If it not inside 
# i would like the programm to start to draw a hangman.

letter_find = "" # Letter find by the player


# Counting the number of attemtps. When attempts = game over
while attempts > 0:
    # Asking player to enter character
    guess = input(f'{user_name} guess a character: {screen} ')
    print(guess)

    if guess in solution: 
        letter_find = letter_find + guess
        print("Good letter, continue", screen, letter_find)

        if letter_find == "God":
            print("you win")
            exit()

    else:
        attempts = attempts - 1
        print(f'wrong letter, {user_name}, try again!, you stil have : {attempts}')

if attempts == 0: 
    print(f'Games over, {user_name} you will do better next time')





    



