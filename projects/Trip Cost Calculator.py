# Trip Cost Calculator
# Create a python script that asks a user questions in the command line. The script should follow the outlined specs.

# Specs
# Receive the following arguments from the user:

# kilometers to drive
# liters-per-kilometer usage of the car
# price per liter of fuel
# Calculate the cost of the trip and display it to the user in the console.

from decimal import Decimal

distance = Decimal(input("How many KM do you drive? "))
fuel_lbykm = Decimal(input(" How much consume your car by KM? "))
fuel_price = Decimal(input("What is the price per liter of fuel ?  "))

costtrip = distance * fuel_lbykm * fuel_price

print(f"the cost of your trip is {costtrip} $")