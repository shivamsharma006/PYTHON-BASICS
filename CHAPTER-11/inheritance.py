class Company:
    company = "ITS"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
    

class Programmer(Company):
    company = "Deloitte"
    language = "Javascript"
    def showlanguage(self):
        print(f"The language is {self.language} and the company is {self.company}")


a = Company()
b = Programmer()
print(a.company,b.company)
