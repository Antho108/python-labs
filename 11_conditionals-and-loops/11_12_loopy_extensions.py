# Proof that the following file is a .pdf file using a `for` loop.
# - Don't use the string method you've used to solve this before!
# - Don't use the `in` keyword to look for a sub-string!
# - Don't use any string slicing technique either!
#
# You'll see that it'll be tricky to solve this challenge with a loop :)
# Remember to use also other techniques you've learned,
# for example flags and conditional statements.

list_1=["document.doc","file.txt","video.mkv", "file2.pdf"]
# filename = "operators.pdf"
Flag = False
ext = ""
pdf_docs = []
for doc in list_1: 
    Flag = False
    ext = ""
    # print(doc)

    for char in doc:        
        if char == "." : 
            Flag = True
      
        if Flag == True:
            ext += char
    if ext == ".pdf":
        pdf_docs.append(doc) 

print(f"the pdf documents are {pdf_docs}")
    

    





    


#  "letter by letter" to "compare 3 letters to another 3 letters"
# letter_list = ["p,d,f"]

# counter = 0
# test = ""

# for char in filename: 
#     if char == "p" or "d" or "f":
#         counter += 1
#         test =+ 1
#         print(test)

# mot = 'operators.pdf'
# compteur = ""
# for lettre in mot:
#     if lettre == 'o':
#         compteur = compteur + 1
# print(compteur)

# index = 0
# while index < len(fruit):
#     lettre = fruit[index]
#     print(lettre)
#     index = index + 1
    
# you need a way to collect the letters into smaller pieces

# Comment vais je prouver que c'est un pdf ? 
# En comparant les lettres 3*3 et en disant voila si tu as ce mot pdf alors tu imprimes que c'est un pdf



# for x in filename: 
#     if x in "pdf" :
#         flag == True
#     print(x)









# file_1 = "operators.pdf"
# files = [file_1]

# for x in files : 
#     if x.endswith(".pdf"):
#         print("goodjob")
#     else: 
#         print("wrongfile")
    

