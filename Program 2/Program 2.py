# Program 2 - Palindromes
# Name: Jackson Hidley
# Date: 10/27/2022


# Print the menu
def printMenu():
    print("---MENU---")
    print("1. Enter integer")
    print("2. Exit program")
    print("Selection: ", end='')

# Get input from the user and check if it is a non-negative integer
def palindromes():
    print("Enter a non-negative integer and I'll tell you if it is a palindrome: ", end='')
    num = int(input())
   
    valid = is_palindromes(num)

    if valid == True:
       palidrome = reverse_digits(num)
       if palidrome == num:
            print("The integer ", num, " is a palidrome")
       else:
            print(num, " is not a palidrome")

       
    elif valid == False:
        print(num, "is not a palidrome.")
    elif valid == 'invalid':
        print("Error! The input is not valid!")
    else:
        print("Validation Error!")


# Calculate if the input is a palidrome recursively

def reverse_digits(num):
    global rev
    print(rev)
    if num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        rev = reverse_digits(num//10)
    else:
        return rev
    return rev

# Check if the user's input is negative
def is_palindromes(num):
    if num >=0:
        return True
    elif num < 0:
        print("Only non-negative integers are accepted!")
        return False
    else: 
        return 'invalid'

# ---MAIN---
while True:
    printMenu()
    menuInput = int(input())

    if menuInput == 1:
        rev = 0
        palindromes()
    elif menuInput == 2:
        break
    else:
        print("Selection must be 1 or 2!")

