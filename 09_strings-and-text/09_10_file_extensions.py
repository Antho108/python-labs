# Use a Python string method to prove which of the following files
# are .pdf files, and which aren't.
# Call the method on each file string and print() Python's response.

file_1 = "operators.pdf"
file_2 = "snowfall.jpg"
file_3 = "uncle-joes-wedding.doc"
file_4 = "invitation.pdf"

# files = [file_1, file_2, file_3, file_4]
# for x in files : 
#     if x.endswith(".pdf"):
#         print("goodjob")
#     else: 
#         print("wrongfile")


file_1 = "operators.pdf"
files = [file_1, file_2, file_3, file_4]

for x in files : 
    if x.endswith(".pdf"):
        print(f' {x} is PDF')
    else: 
        print(f' {x} is not PDF')

# Collect user files
# NEW --> Convert user input to lowercase
# Compare to the string "something"
# Print a win or lose message



