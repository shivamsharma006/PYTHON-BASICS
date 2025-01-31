a=89

def fun():
    # by defining any variable global, it changes it's global value 
    global a
    a=3
    print(a)


fun()
print(a)
