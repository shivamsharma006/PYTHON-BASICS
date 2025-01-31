# Write a recursive function to calculate the sum of first n natural numbers.

def sumNaturalNumber(n):
    if(n==1):
        return 1
    return sumNaturalNumber(n-1)+n

n = int(input("Enter a no: "))
print(sumNaturalNumber(n))