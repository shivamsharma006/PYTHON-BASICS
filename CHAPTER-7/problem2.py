''' Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
'''
l = ["Harry", "Soham", "Sachin", "Rahul"]
n = len(l)
for i in range(n):
    if(l[i].startswith("S")):
        print(l[i])