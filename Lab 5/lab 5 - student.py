## Lab 5 - Lists
# Name: Jackson Hidley
# Date: 11/8/2022

'''
You have been tasked with writing some software for the Pizza Palace, an exciting new pizza crafting and consuming joint.
Please finish the software by writing code under the commented areas below.

Thanks! 
- Management
'''

#orders given to you by the system. Only use this to append to your list below.
from tkinter import N


incoming_orders = [["Steve",2,"Old Fashioned"],["Sherry",1,"Old Fashioned",2,"Veggie"],["Kevin",1,"Veggie"],["Travis",14,"Old Fashioned",28,"Veggie"],["Jeremy",4,"Old Fasioned",8,"Veggie"]]

#your order list to work with
orders = []


#use a for loop to append each item from incoming_orders to orders
for order in incoming_orders:
    orders.append(order)

#use a while loop to display the first 3 orders from the list.
#ask the user to input the character 'n'. 
# if 'n' is pressed then use the list method pop to remove item 0 from the list.
#use if statement blocks to determine if there are even 3 items in the list
#if the length of orders is less than 3 items, display all current orders
#you can check length using len(orders)
#if there are 0 orders, break.
while(True):
    if len(orders) >= 3:
        print(orders[0:3])
    elif len(orders) == 2:
        print(orders[0:2])
    elif len(orders) == 1:
        print(orders[0:1])
    elif len(orders) == 0:
        break
    else:
        print(len(orders))
        print("Error")

    user_input = input("Press n to pop list: ")
    if user_input =='n' or user_input == 'N':
        orders.pop(0)