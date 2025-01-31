'''
Write a python function to print first n lines of the following pattern:
***
** 
*
for n = 3
'''
def printPattern(n):
    if(n==0):
        return
    print("*" * n)
    return printPattern(n-1)

n = int(input("Enter a no: "))
print(printPattern(n))