'''
Write a program to find out the line number wher Twinkle is present from ques 6.
'''
with open("poem.txt") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if("Twinkle" in line):
        print(f"Yes present at line no: {lineno}")
        break
    lineno+=1
else:
    print("Not present")




