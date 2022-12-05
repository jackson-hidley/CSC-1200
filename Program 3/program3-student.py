#Program 3
#Name: Jackson Hidley
#Date: 12/2/2022

############### functions 

# function to print the menu - DONE
def print_menu():
    print("TN Tech University Student Database")
    print("Please make a selection:")
    print("1. View all current students")
    print("2. Enter new student data")
    print("3. Remove student data")
    print("4. Modify student data")
    print("5. Quit")

    return


# function to add a new student to the dictionary
# needs to take in new user data and then return full, updated dictionary
#check if user exists, if not, add user
def add_student(student_data):
    tNum = input("T number of student: ")
    name = input("Name of student: ")
    user = input("Username of student: ")
    clas = input("Class of student: ")
    if tNum in student_data:
        print("Student already exists.")
    else:
        student_data[tNum] = {'NAME': name, 'USERNAME': user, 'CLASS': clas}

    if tNum in student_data:
        print("Student added")
        return student_data
    else:
        print("T number already exists.\nStudent was not added")
    return student_data
    
# function to modify student data
# needs to take in current user t-num and then re-enter fields and then return updated dictionary
#check if user exists, if it does, modify that user
def modify_student(student_data):
    print_data(student_data)
    tNum = input("Enter the T number of the student that you want to remove: ")
    if tNum in student_data:
        student_data.pop(tNum)
        print("Modifying student: ", tNum)
        
        name = input("Name of student: ")
        user = input("Username of student: ")
        clas = input("Class of student: ")

        student_data[tNum] = {'NAME': name, 'USERNAME': user, 'CLASS': clas}

    else:
        print("Student does not exist")
    
    return student_data

def print_data(student_data):
    for tNum, value in student_data.items():
        print(tNum)
        print("****")

        for key in value:
            print(key + ':', value[key] + '\n')
        
    return

def remove_student(student_data):
    print_data(student_data)
    tNum = input("Enter the T number of the student that you want to remove: ")
    if tNum in student_data:
        student_data.pop(tNum)
        print("Removed student T-number ", tNum)
    else:
        print("Student does not exist")
    return student_data

# student dictionary that I am providing. This will be your main student database.
student_data={"T123":{"NAME":"Travis Lee", "USERNAME":"tlee", "CLASS":"Senior"},"T124":{"NAME":"Jeremy Potts", "USERNAME":"jpotts", "CLASS":"Freshman"}}

# in a while loop, print the menu and take in a user menu choice
# using if statements, create options for viewing users, adding users, removing users, modifying users, and ending the program.


#___Main___
while(True):
    print_menu()

    choice = int(input("Selection: "))

    if choice == 1:
        print_data(student_data)
    elif choice == 2:
        student_data = add_student(student_data)
    elif choice == 3:
        student_data = remove_student(student_data)
    elif choice == 4:
        student_data = modify_student(student_data)
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid input. Try again.")


