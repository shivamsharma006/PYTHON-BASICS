class Employee:
    language = "English"
    salary = 1200000

    def getInfo(self):
        print(f"The language is : {self.language}. The salary is {self.salary}")

    @staticmethod #static method does not use any method(self)
    def greet():
        print("Good Morning!")

harry = Employee()
harry.language = "Python"

harry.greet()

harry.getInfo()