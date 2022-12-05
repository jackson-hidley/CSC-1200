## Lab 3 - Can I get uhhhh...
# Name: Jackson Hidley
# Date: 9/22/2022

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
def build_combo( crust, topping1, topping2, topping3 ):
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

# variable for keeping track of the order total
total = 0

# Main
######################################################

# Printing a greeting for the customers
print_greeting()


# ToDo: Create a variable, num_pizzas and assign it a value from user input with the prompt: "How many pizzas will you be ordering today?: "
print("How many pizzas will you be ordering today?: ", end="")
num_pizzas = int(input())


# ToDo: Create a for loop that runs for a range of num_pizzas
# Inside the for loop you will use print_menu() and create a variable order_num that will be assigned a value of user input with the prompt: "Please make a pizza selection: "
# Inside the for loop you will then use if elif statements to decide which build_combo should be ran.
# when running build_combo, you will take your current total and assign it a value of itself + build_combo. Just like last lab.
# below is psuedo code DO NOT just copy paste this code. It doesn't run. It is psuedo code to guide you.
# for num_pizzas:
#   display menu
#   order = user input
#       if order == 1:
#           total = total + build_combo(old_fashioned)     
#       else: print "Not an option!"

# you should have 1 if, 2 elif, and 1 else. 

for i in range(num_pizzas):
    print_menu()
    print("Choice: ", end="")
    order = int(input())
    # If old fashioned is selected
    if order == 1:
        total += build_combo(crust_thick,pepperoni,cheese,mushrooms)
    # If Veggie is selected
    elif order == 2:
        total += build_combo(crust_thin,spinach,mushrooms,peppers)
    # If Meat is selected
    elif order == 3:
       total += build_combo(crust_thick,pepperoni,cheese,sausage)
    # Incorrect selection
    else:
        print("Not an option!")



# ToDo print a message and the num_pizzas ordered for the customer using print, and then print the total using our print_price function.
print("You have ordered " , num_pizzas, " pizza(s) The total is: ", end="")
print_price(total)


