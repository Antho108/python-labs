# Population Growth Calculator
# Write the necessary code to display the total population count for the next 3 years (without a leap year).

# Here are the specifications:

# In the country we want to investigate:

# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds

# # We want to know the population for the next 3 years.
# basepopulation = 380.123.456

# Every seconds basepopulation + 6 
# Every 12 seconds basepopulation  - 12 
# Every 48 seconds basepopulation + 48 sec

# Naissance par an 
# secondesyears = 60*60*24*365
# print(secondesyears) # 31536000
basepopulation = 380123456
pbornbyear = (31536000 / 6)  # 5 256 000
pimmigratebyear = (31536000 / 48) # 657 000
plessbyear = 31536000 / 12 # 2 628 000

pmorebyyear = (pbornbyear + pimmigratebyear) - plessbyear # 3 285 000 
pmore3year = pmorebyyear * 3 # 9 855 000
finalpopulation = pmore3year + basepopulation
print (finalpopulation) # 389 978 456
