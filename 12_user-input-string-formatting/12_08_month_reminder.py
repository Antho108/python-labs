# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.



user = int(input("Choice a number"))
number_list = [1,2,3,4,5,6,7,8,9,10,11,12]
month_list = ["January", "February"]
print(month_list[0])


while user not in number_list:
    print ("Error wrong number start again") 
    break

if user == 1: 
    print ("The month is January")

if user == 2: 
    print ("The month is February")

if user == 3: 
    print ("The month is March")

if user == 4: 
    print ("The month is April")

if user == 5: 
    print ("The month is Mai")

if user == 6: 
    print ("The month is June")

if user == 7: 
    print ("The month is July")

if user == 8: 
    print ("The month is August")

if user == 9: 
    print ("The month is September")

if user == 10: 
    print ("The month is October")

if user == 11: 
    print ("The month is November")

if user == 12: 
    print ("The month is December")




# print(f"Your number {user} is this {month}")

