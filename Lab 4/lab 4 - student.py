## Lab 3 - I Want Uhhhh...
# Name: Jackson Hidley
# Date: 10/6/2022

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
    print("***************")

# function to do combos
# ToDo - add default parameters for topping 2 and 3. Make the default be 0.
def build_combo( crust, topping1, topping2 = 0, topping3 = 0 ):
    price = crust + topping1 + topping2 + topping3
    return price

# function to print prices
def print_price(price):
    print("$"+str(round(price,2)))

# function to print a menu
def print_menu():
    print("1. Old Fashioned")
    print("2. Veggie For Days")
    print("3. Meat Lovers")
    print("4. Cheese")
    print("5. Done")


    

# Variables
######################################################


crust_thick = 0.58
crust_thin = 0.48
pepperoni = .30
cheese = .35
mushrooms = 1.00
spinach = 0.45
peppers = 0.20
sausage = 1.20

# variable for keeping track of the order total and number of pizzas ordered
total = 0
num_pizzas = 0

# Main
######################################################

# Printing a greeting for the customers
print_greeting()




# ToDo: Modify the for loop to be a while loop that check is the variable x is True. You will have to create this variable and set it to True initially
# ToDo: Add elif statements for the additional items in the print_menu() function above.

# below is psuedo code DO NOT just copy paste this code. It doesn't run. It is psuedo code to guide you.
# while x is True:
#   display menu
#   order = user input
#       if order == 1:
#           total = total + build_combo(old_fashioned)
#           num_pizzas = num_pizzas + 1
#       elif done: x = False     
#       else: print "Not an option!"

# you should have 1 if, 4 elif, and 1 else.
x = True

while(x):

    print_menu()
    order = int(input("Please make a pizza selection: "))

    if order == 1:
        total = total + build_combo(crust_thick,pepperoni,cheese,mushrooms)
        num_pizzas += 1

    elif order == 2:
        total = total + build_combo(crust_thin,spinach,mushrooms,peppers)
        num_pizzas += 1

    elif order == 3:
        total = total + build_combo(crust_thick,pepperoni,cheese,sausage)
        num_pizzas += 1

    elif order == 4:
        total = total + build_combo(crust_thick,cheese)
        num_pizzas += 1
        
    elif order == 5:
        x = False
    else: print("Not an option!")


# ToDo print a message and the num_pizzas ordered for the customer using print, and then print the total using our print_price function.
print("Your total for ", num_pizzas, " pizzas is: ", end='')
print_price(total)


