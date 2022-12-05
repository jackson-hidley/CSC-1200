## Program 1 - Squares
# Name: Jackson Hidley
# Date: 09/20/2022

# Get input from user and pass it print_2byN
def call_2byN():
    print("What is n value for 2byN?: ")
    n = int(input())
    print_2byN(n)

# # Get input from user and pass it to print_4byN
def call_4byN():
    print("What is n value for 4byN?: ")
    n = int(input())
    print_4byN(n)

# Get 2 inputs from user and pass it to print_MbyN
def call_MbyN():
    print("What is m value for MbyN?: ")
    m = int(input())

    print("What is n value for MbyN?: ")
    n = int(input())
    print_MbyN(m,n)

# Print 2 columns with N rows
def print_2byN(n):
    print_MbyN(2,n)

# Print 4 columns with N rows
def print_4byN(n):
    print_MbyN(4,n)

# Print M columns with N rows
def print_MbyN(m,n):
    i = 0
    for i in range(m):
        print("+----------" * n, "+")
        print("|          " * n, "|")
        print("|          " * n, "|")
        print("|          " * n, "|")
            
    #Print last line
    print("+----------" * n, "+")
    

call_2byN()
call_4byN()
call_MbyN()