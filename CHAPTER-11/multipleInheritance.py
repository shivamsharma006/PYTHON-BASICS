class Company:
    company = "ITS"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")
    
class Coder:
    language = "Javascript"
    def printLanguages(self):
        print(f"Out of all languages here is ur language: {self.language}")

class Programmer(Company,Coder):
    company = "Deloitte"
    def showlanguage(self):
        print(f"The language is {self.language} and the company is {self.company}")


a = Company()
b = Programmer()

b.show()
b.showlanguage()
b.printLanguages()