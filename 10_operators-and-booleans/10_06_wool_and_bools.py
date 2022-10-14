# Write a code snippet that gives a name to a `sheep`
# and uses a boolean value to define whether it has `wool` or not.
have_wool = False
sheep_name = input("quel est le nom de ton mouton? ") 

if len(sheep_name)>=5:
    have_wool = True

if have_wool==True:
    print('have wool')
else:
    print ('no wool')


