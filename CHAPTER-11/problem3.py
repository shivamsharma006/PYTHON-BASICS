'''
Create a class ‘Employee’ and add salary and increment properties to it

Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
which changes the value of increment based on the salary.
'''

class Employee:
    salary = 3000
    increment = 30

    @property
    def salaryAfterIncrement(self):
        return (self.salary+self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment  = ((salary/self.salary)-1)*100

e = Employee()
e.salaryAfterIncrement = 280
print(e.increment)