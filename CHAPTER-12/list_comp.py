"""mylist = [23,244,24,4]

squaredList = []

for i in mylist:
    squaredList.append(i*i)

print(squaredList)"""

mylist = [23,244,24,4]
squaredList = [i*i for i in mylist]
print(squaredList)