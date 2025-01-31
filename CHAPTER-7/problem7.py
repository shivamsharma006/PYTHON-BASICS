'''
Write a program to print the following star pattern.
 *
***
***** for n = 3
'''

n = 3
for i in range(1,n+1):
    print(" " * (n-i),end="") # By using end, new line can't come
    print("*" * (2*i-1),end="") # By using end, new line can't come
    print('\n')