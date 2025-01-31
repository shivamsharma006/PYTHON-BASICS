'''
f = open("file.txt")
print(f.read())
f.close()
'''

# We can do the same function by using the with function
with open("file.txt") as f:
    f.read()
    # There's no need to close the file