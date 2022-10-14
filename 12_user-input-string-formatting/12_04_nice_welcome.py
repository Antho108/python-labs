# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


first_name = input("What is your firstname? ")
last_name = input("What is your lastname ?")

print(f"Welcome mister {first_name}")
