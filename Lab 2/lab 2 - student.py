## Lab 2 - How many pizzas?
# Name: Jackson Hidley
# Date: 09/08/2022

'''
You have been tasked with writing some software for the Pizza Palace, an exciting new pizza crafting and consuming joint.
Please finish the software by writing code under the commented areas below.

Thanks! 
- Management
'''
# Functions
######################################################

# function to print a cool little welcome message
def print_greeting():
    print("Welcome to the Pizza Palace!")
    print("Your total is below")
    print("***************")

# function to do combos
# ToDo: return the variable 'price'
def build_combo( crust, topping1, topping2, topping3 ):
    price = crust + topping1 + topping2 + topping3
    return price

# function to print prices
def print_price(price):
    print("$"+str(round(price,2)))


# Variables
######################################################


# Thick Crust   - $0.58
# Thin Crust    - $0.48
# Pepperoni     - $0.30
# Cheese        - $0.35
# Mushrooms     - $1.00
# Spinach       - $0.45
# Peppers       - $0.20
# Sausage       - $1.20

crust_thick = 0.58
crust_thin = 0.48
pepperoni = .30
cheese = .35
mushrooms = 1.00
spinach = 0.45
peppers = 0.20
sausage = 1.20

## Number of each combo the customer wants to order
old_fashioned = 3
veggie = 4
meat_lovers = 1

# Main
######################################################


print_greeting()

# Old Fashioned
print("Old Fashioned - ", end='')

# ToDo: 
# Put build_combo in a for loop using the number of pizzas ordered variable above in range()
# This for loop will have a variable old_fashioned_price that is assigned a value of itself + build_combo
# You will then use print_price to print the new price OUTSIDE of the for loop 
# example 
# for pizza in range(num_pizzas):
#   do stuff here
old_fashioned_price  = 0
for pizza in range(old_fashioned):
    old_fashioned_price += build_combo(crust_thick,pepperoni,cheese,mushrooms)
print_price(old_fashioned_price)

# Veggie For Days
print("Veggie For Days - ", end='')

# ToDo: 
# Put build_combo in a for loop using the number of pizzas ordered variable above
# This for loop will have a variable veggie_price that is assigned a value of itself + build_combo
# You will then use print_price to print the new price OUTSIDE of the for loop
#build_combo(crust_thin,spinach,mushrooms,peppers)
veggie_price = 0
for pizza in range(veggie):
    veggie_price += build_combo(crust_thin,spinach,mushrooms,peppers)
print_price(veggie_price)

# Meat Lovers
print("Meat Lovers - ", end='')

# ToDo: 
# Put build_combo in a for loop using the number of pizzas ordered variable above
# This for loop will have a variable meat_price that is assigned a value of itself + build_combo
# You will then use print_price to print the new price OUTSIDE of the for loop
meat_price  = 0
for pizza in range(meat_lovers):
    meat_price += build_combo(crust_thick,pepperoni,cheese,sausage)
print_price(meat_price)
