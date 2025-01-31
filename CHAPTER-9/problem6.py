'''
Write a program to mine a log file and find out whether it contains ‘Twinkle’.
'''

with open("poem.txt") as f:
    content = f.read()

if("Twinkle" in content):
    print("Yes present")
else:
    print("Not present")