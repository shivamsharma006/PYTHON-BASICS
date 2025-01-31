class Employee:
    name = "Amit"
    language = "English"
    salary = 1200000

harry = Employee()
print(harry.name,harry.language)

rohan = Employee()
print(rohan.language,rohan.salary)
rohan.name = "Robinson Kafi" #This is an instance attribute
print(rohan.name)

print(harry.name)