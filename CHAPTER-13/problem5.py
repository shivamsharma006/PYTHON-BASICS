'''
Write a program to find the maximum of the numbers in a list using the reduce 
function.
'''
from functools import reduce

a = [24,423,424,4,24,5,55,34234,3445]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))