# Write a python function which converts inches to cms.

def inch_to_cm(inch):
    return inch * 2.54

inch = int(input("Enter inches: "))
print(f"After converting into cm: {inch_to_cm(inch)}cm")