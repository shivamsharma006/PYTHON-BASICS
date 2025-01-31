'''
f = open("file.txt")
r = f.readlines()
print(r, type(r))
f.close() 
'''

# WITHOUT USING A WHILE LOOP
'''
f = open("file.txt")

r1 = f.readline()
print(r1, type(r1))

r2 = f.readline()
print(r2, type(r2))

r3 = f.readline()
print(r3, type(r3))

f.close() 
'''

# USING A WHILE LOOP
f = open("file.txt")
r = f.readline()
while(r!=""):
    print(r)
    r = f.readline()
f.close()