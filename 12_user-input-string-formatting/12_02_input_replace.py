# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please


user = input("say a word ")
symbol = str(input("Enter a symbol "))

print(f"your message is {user} and your symbol is {symbol}")

new_user= user.replace({symbol}, 'm')
print(new_user)


print(f"your new message is {new_user}")