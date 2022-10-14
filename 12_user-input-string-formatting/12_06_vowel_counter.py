# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

vowels_list = ["a","e","i","o","u"]


counter = 0
toto = 0
ioio = 0 
ouou= 0 
uuuu = 0 



sentence = input("Write your sentence!")

for a in sentence:
   if a == "A" or "a": 
    counter += 1
   
for e in sentence:
    if e == "E" or "e":
     toto += 1 

for i in sentence:
    if i == "I" or "i":
     ioio += 1 

for o in sentence:
    if o == "O" or "o":
     ouou += 1 

for u in sentence:
    if u == "U" or "u":
     uuuu += 1 


print(f"The number of vowel A is {counter} vowel E is {toto} vowel I is {ioio} vowel O is {ouou} U is {uuuu}  ")

