# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

user = input("Give me your honest opinion ")
print(f"the user message is {user}")
new_user = ""

for i,x in enumerate(user):
    if (i%2 == 0):
        new_user += user[i].upper()
    else:
        new_user += user[i].lower()
print(new_user)


