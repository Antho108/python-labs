# Your hunger-meter currently only handles string input accurately.
# Replace your first `if` statement with a type check.
# If the value of `hunger` is not of the type `str`,
# print a message that reminds you to
# declare your hunger levels with a string.

# input("your hunger leve l")
hunger = input("your hunger level")

if hunger in ["small","big"]:
    hunger=input("Declare your hunger only by big or small")
    

if hunger == "big" :
    print("Eat the pizza")
elif hunger == "small":
    print("Eat the apple")
else:
    print("Don't eat anything")


