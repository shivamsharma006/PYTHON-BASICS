'''
Write a program to accept marks om 6 students and display them in a sorted 
manner.
'''
marks = []
m1 = int(input("Enter marks:"))
marks.append(m1)
m2 = int(input("Enter marks:"))
marks.append(m2)
m3 = int(input("Enter marks:"))
marks.append(m3)
m4 = int(input("Enter marks:"))
marks.append(m4)
m5 = int(input("Enter marks:"))
marks.append(m5)
m6 = int(input("Enter marks:"))
marks.append(m6)
m7 = int(input("Enter marks:"))
marks.append(m7)

marks.sort()
print(marks)