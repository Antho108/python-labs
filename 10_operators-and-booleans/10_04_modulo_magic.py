# Use the modulo operator to confirm which of the values
# shown below are divisible by seven.
num_1 = 42
num_2 = 137
num_3 = 455
num_4 = 1997

list_number = [num_1,num_2,num_3,num_4]

for x in list_number: 
    if x%7 == 0:
        print(f'{x} is divisible by 7')
    else:
        print(f'{x} is not divisible by 7')
