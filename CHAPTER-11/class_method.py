class Employee:
    a=1
    
    @classmethod
    def show(cls):
        print(f"The value of a is :{cls.a}")

e = Employee()
e.a = 23
e.show()
