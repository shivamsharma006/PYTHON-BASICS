class Employee:
    a=3
class Programmer(Employee):
    b=4

class Manager(Programmer):
    c=5

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is no b attribute in Employee class

o = Programmer()
print(o.a,o.b)

o = Manager()
print(o.a, o.b, o.c)