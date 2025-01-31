# Write a program using functions to find greatest of three numbers.


def findGreatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    elif(c>a and c>b):
        return c

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
print(f"Greatest number is {findGreatest(a,b,c)}")