try:
    a = int(input("Hey,Enter a number: "))
    print(a)


except Exception as e:
    print(e)
# When try becomes successfull then else part will work otherwise not
else:
    print("I am inside else")