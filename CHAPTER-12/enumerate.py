"""l = [32,442,3,255]

index = 0
for item in l:
    print(f"The item number {index} is {item}")
    index+=1
"""
l = [32,442,3,255]

for index,item in enumerate(l):
    print(f"The item number {index} is {item}")