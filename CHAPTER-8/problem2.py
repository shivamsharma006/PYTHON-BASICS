# Write a python program using function to convert Celsius to Fahrenheit

def f_to_c(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
print(f"After conversion into C = {f_to_c(f)}°C")