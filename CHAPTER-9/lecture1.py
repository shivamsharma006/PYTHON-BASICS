# st = "Hey Shivam you are a good boy"

# f = open("myfile.txt" ,"w")
# f.write(st)
# f.close()

f = open("myfile.txt")
data = f.read()
print(data)
f.close()