# Print out every prime number between 1 and 1000.

# n=int(input("Choice a number to check if is prime "))

    
def is_Prime(n):
    decision=False
    for x in range(2,n):
        if n%x == 0: 
            # print("is not prime")
            decision=False
            break
        elif n%x != 0 and x==n-1: 
        #  print("is prime")
         decision=True
    return(decision)

prime_list =[]

for x in range(1,1001):
    if is_Prime(x):
       prime_list.append(x)
print(prime_list)

# num = 1000
# for i in range(1,num+1):
#     is_prime = True
#     for j in range(2,i):
#         if i % j == 0 : 
#             is_prime = False
#     if is_prime:
#         print(i)

