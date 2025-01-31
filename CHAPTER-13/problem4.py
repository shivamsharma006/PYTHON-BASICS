'''
Write a program to filter a list of numbers which are divisible by 5.'''


def divisible5(n):
    if(n%5==0):
        return True
    return False

a = [24,423,424,4,24,5,55,34234,3445]

f = list(filter(divisible5,a))
print(f)