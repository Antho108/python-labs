# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.

# ---------------------------- Chapter 2 -----------------------------

# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.


# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
my_choice = set()


# Var
my_inventory = list()
sword = None 
fight_dragon = None
equipement = None
bow_selection = None
flag = True
special_ring = None



# Ask the player for their name.
player_name = input(" Enter your name ! ")


# Display a message that greets them and introduces them to the game world.
print(f"""Dungeon & Dragons 2 ! Welcome {player_name}, who has just defied the dragon in his dungeon!
 Go through the dungeon and get the infinity sword and other items to defeat the dragon! Good luck to you """)




# Asking the user to stuff is character. 
print(f""" {player_name} Go through the amurerie and get equipped! On your choice will depend the victory!  """)


# User Items
print(f"What do you like ?")


while equipement not in { "A", "a", "B", "b", "C", 'c'}:

    equipement = input(str(f' A - Hammer, B - Magic Cloak , C - Magician Stick '))

    if equipement in {"A", 'a'}:
        my_inventory.append(" Hammer ")

    if equipement in {"B", 'b'}:
        my_inventory.append(" Magic Cloak ")

    if equipement in {"C", 'c'}:
        my_inventory.append(" Magician Stick ")
    
    item = my_inventory[0]

print(f'Dear {player_name}, you are equipped with {item} , Good luck !')


# Starting point of the Dongeon, multi choice. 
while flag == True:
    doors_selection = input(" Choose your direction enter left, right, center, top, down ! To check invetory, tape inv  ")
    my_choice.add(doors_selection)


# If they choose the left door, they'll see an empty room.
    if doors_selection in {"left"} :
       print(f' You are in the empty room' )
      
# Center section. Bow. 
    if doors_selection in {"center"}: 
        print(" The door is close. The dead have barred the door. On the door there is a Bow do you want to take it ? ")
        bow_selection = input(str(" A - Yes -, B - No - "))
        
        if bow_selection in {"A", 'a'}:
             my_inventory.append("Bow")
             print(f" With this bow, {player_name} you can kill the Gobelin. ")
        else: 
             print(f" I hope you have a weapon for survive in the dongeon")


# Gobelin section    
    if doors_selection in {"top"}:
        print(" This area is The Gobelin Silver, be sure to have a weapon! ")
        gob_place = input(str(" Do you feel ready to go the Gobelin Silver Area ? Yes or No ? "))
    
        if gob_place in {"Yes", "yes"} and  my_inventory: 
            print(f" With the help of your {my_inventory}, You kill all the weak goblin !!!")
            print(f' Special ring for you + 5 attack ')
            my_inventory.append(" Special Ring ")
            special_ring = True
        
        if gob_place in {"Yes", "yes"} and not my_inventory: 
            print(f' You are escaping from death lucky boy, go back and take a weapon')

            
# If they choose the right door, then they encounter a dragon.
    if doors_selection in {"right"} :
        
        print(f' This room is guard by the Dragoon. If you want to win, you need to have a sword and the special ring.')
        fight_dragon = input(" Are you ready to fight, yes or no ? ")
        
# Modify inventory.  
# # Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.       
    if doors_selection in {"inv"} :
            print(f' This is your inventory {my_inventory}') 
            while doors_selection == "inv":
                print(" Which items do you want to remove ?")
               
                clear_inv = input(str(f'  A - Hammer, B - Magic Cloak , C - Magician Stick , D - Clear All - E Just pass '))

                
                if clear_inv in {"A", 'a'}:
                    my_inventory.remove(" Hammer ")
                    break

                if clear_inv in {"B", 'b'}:
                    my_inventory.remove(" Magic Cloak ")
                    break

                if clear_inv in {"C", "c"}:
                    my_inventory.remove(" Magician Stick ")
                    break
                
                if clear_inv in {"D", 'd'}:
                    my_inventory.clear()
                    break
                
                if not my_inventory : 
                    print(' Your inventory is empty ')
                    break

                else: 
                    print(f'This is your items in your {my_inventory}')
                    break
                    
            
# When encountering the dragon, they have the choice to fight it. Only with sword = loose
    if fight_dragon in {"yes"} and sword == None :
            
            print("The dragon is to strong, you die, come back next time with a magic sword! ")
            my_inventory.clear()
            print(f" You drop all your items and lost your {my_inventory} ")
            exit("Game over")

# When encountering the dragon, they have the choice to fight it. Sword or ring = loose 
    if fight_dragon in {"yes"} and sword == True and special_ring == None :
            
            print("The dragon is to strong, you die, come back next time with a magic sword and your ring ! ")
            my_inventory.clear()
            print(f" You drop all your items and lost your {my_inventory} ")
            exit("Game over")

# If they have the sword from the other room, then they will be able to defeat it and win the game.
    if fight_dragon in {"yes"} and sword == True and special_ring == True:
            
            print(f'You meet the dragon and kill him with your sword and ring! Congratulations {player_name} ')
            exit(f'You win')


# If they don't have the sword, then they will be eaten by the dragon and lose the game.
    if fight_dragon in {"no"} :
        door_selection = None
        level_selection = None
        flag = True 
    pass


# Selection level      
    level_selection = input("Do you wish to  - look around - or  - to go back ? ")
    my_choice.add(level_selection)

# Way to take the sword    
    if level_selection in {"look around"} : 
        
        print(f"Dear {player_name} it's look like, there is sword. ")
        sword_selection = input(" The power of the sword can kill a dragon - Choice A - Take it - or B - Leave it - ")

        if sword_selection in {"A", 'a'}: # "Take it"
          
            my_inventory.append(" SwordDragon ")
            sword = True 
            flag == True
            print(f'Dear {player_name} you are now ready to fight the Dragon, you get the magic sword!')
          
            #Encouter the dragon 
            if  sword_selection in {"B" or "b"}:  # "Leave it"
                sword = None 
                flag = False
                pass
                # Go back to the two doors. 
    else: pass
     
        
print("im outside of the game")
            








