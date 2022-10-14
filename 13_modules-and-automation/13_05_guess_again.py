# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random

num = random.randint(1, 10)
guess = None 
tries = 0 # Let's say you have only 3 tries

while guess != num : 
    guess = int(input("Guess a number between 1 and 10 please "))
    tries += 1
    if guess == num : 
        print("Bravo you win")
       
        break 
    elif tries >= 2 : 
        print("Game Over")
        exit()

  
    else : 
        print("Try Again, last chance")
        
        
# Je veux donner 3 chances à la personne. Au bout des 3 chances, je veux que le jeu s'arrete
# "et que un message Game Over s'affiche "
# J'aimerais par exemple que l'ordinateur dise à l'utilisateur vous n'avez plus que 1 chance 