class Employee:
    language = "English"
    salary = 1200000

        
    def greet(self):
        print("Good Morning!")

    def getInfo(self):
        print(f"The language is : {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "Python"

harry.greet()

harry.getInfo()