# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Harry",13394,203001)
print(p.name,p.salary,p.company,p.pin)


r = Programmer("Shivam",188888,203003)
print(r.name,r.salary,r.company,r.pin)