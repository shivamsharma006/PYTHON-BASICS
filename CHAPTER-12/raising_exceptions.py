a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))

if(b==0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")
else:
    print(f"The divison a/b is {a/b}")
