def convert24(str1):

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]

    elif str1[-2:] == "AM":
        return str1[:-2]

    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]

    else:
        return str(str1[:2] + 12) + str1[2:-2]
# Creating minute function
def minute(x):
    #changing time to 24 hour format
    first_clock=convert24(x[:7])
    Second_clock=convert24(x[-7:])

    #changing hour to minute
    first_clock_minutes=int(first_clock[:2])*60+int(first_clock[-2:])
    Second_clock_minutes=int(Second_clock[:2])*60+int(Second_clock[-2:])

    #calculating minute differences
    if first_clock_minutes > Second_clock_minutes:
        return (24*60-first_clock_minutes+Second_clock_minutes)
    return Second_clock_minutes-first_clock_minutes

# Enter the input in the form 10.00AM-11.00AM
x=input()
print(minute(x))