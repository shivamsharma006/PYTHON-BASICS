from functools import reduce
# MAP example

l = [1,2,3,4,5]
square = lambda x : x*x

sqlist= map(square,l)
print(list(sqlist))

# Filter Example
def even(n):
    if(n%2==0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

# Reduce Example
def sum(a,b):
    return a+b

print(reduce(sum,l))