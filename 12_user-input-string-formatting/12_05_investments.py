# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.


investment_amount = int(input("What is your investment amount?"))
investment_rate = int(input("What interest rate in percentage?"))
investment_years = int(input("How many years did you invest?"))


futur_value = investment_amount * (investment_rate/100) * investment_years
print(f"Your futur value is {futur_value} dollars")


investment_amount = float(input("What is your investment amount? "))
investment_rate = float(input("What is the interest rate in percentage? "))
investment_years = int(input("How many years did you invest? "))

future_value = investment_amount * (1 + investment_rate/100)**investment_years

print(f"Your future value is {future_value:.2f} dollars")
