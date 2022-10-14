# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

vowels_list = ["a","e","i","o","u"]

a = lorem_ipsum.count('a')
e = lorem_ipsum.count('e')
i = lorem_ipsum.count('i')
o = lorem_ipsum.count('o')
u = lorem_ipsum.count('u')

total_vowels = a + e + i + o + u 
print(f"The total of vowels is {total_vowels}")

counter = 0

for char in lorem_ipsum:
    if char in vowels_list:
        counter += 1
print(f"The total of vowels is {counter}")
        

# print(f"hello {name} i hope good day")