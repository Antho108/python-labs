# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

first = input("Write your first sentence ")
second = input("Write your second sentence ")
third = input("Write your third sentence ")

if len(first) > len(second) and len(first) > len(third): 
      print(len(first), {first})
    
if len(second) > len(first) and len(second) > len(third):
      print(len(second), {second})

if len(third) > len(second) and len(third) > len(first):
      print(len(third), {third})




