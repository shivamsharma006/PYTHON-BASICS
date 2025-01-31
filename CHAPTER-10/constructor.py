class Employee:
    name = "Harry"
    language = "English"
    salary = 1300000

    def __init__(self,name,salary,language):
        self.salary = salary
        self.language = language
        print("hey i am python") #dunder method which is automotically call 
        
    def greet(self):
        print("Good Morning!")

    def getInfo(self):
        print(f"The language is : {self.language}. The salary is {self.salary}")

harry = Employee("harry",120000,"Javascript")
print(harry.name,harry.salary,harry.language)