## Lab 1 - The Pizza Palace
# Name: Jackon Hidley
# Date: 09/01/2022

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
    print("Our menu is as follows:")
    print("***************")

# function to do combos
# ToDo: Make variable price and set price equal to sum of ingredients.
def build_combo( crust, topping1, topping2, topping3 ):
    price = crust + topping1 + topping2 + topping3
    print_price(round(price,2))

# function to print prices
# ToDo: This is broken. Maybe try casting price to string? hmm..
def print_price(price):
    print("$"+str(price))

# Variables
######################################################
# ToDo: We need variables for the following items with prices:

# Thick Crust   - $0.58
# Thin Crust    - $0.48
# Pepperoni     - $0.30
# Cheese        - $0.35
# Mushrooms     - $1.00
# Spinach       - $0.45
# Peppers       - $0.20
# Sausage       - $1.20

thick_c = 0.58
thin_c = 0.48
pepperoni = .30
cheese = 0.35
mush = 1.00
spin = 0.45
peppers = 0.20
sausage = 1.20

# Main
######################################################

# ToDo: Print a welcome message using function
print_greeting()

# Old Fashioned
print("Old Fashioned - ", end='')

# ToDo: build combo
# Old Fashioned ingredients: thick crust, pepperoni, cheese, and mushrooms
build_combo(thick_c, pepperoni, cheese, mush )

# Veggie For Days
print("Veggie For Days - ", end='')

# ToDo: build combo
# Veggie For Days ingredients: thin crust, spinach, mushrooms, and peppers
build_combo(thin_c, spin, mush, peppers)

# Meat Lovers
print("Meat Lovers - ", end='')

# ToDo: build combo
#Meat Lovers ingredients: thick crust, pepperoni, cheese, and sausage
build_combo(thick_c, pepperoni, cheese, sausage)
