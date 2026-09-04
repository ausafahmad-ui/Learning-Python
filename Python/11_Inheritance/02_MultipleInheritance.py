class Employee:
    company="Ethara"
    def show(self):
        print(f"The name of the Employee's company is {self.company}.") 

class Coder:
    language="Python"
    def printLanguage(self):
        print(f"Out of all languages here is your language; {self.language}")

class Programmer(Employee,Coder):
    company="Kubera"
    def showLanguage(self):
        print(f"The name of the employee's comp is {self.company} and the lang is {self.language}")


a=Employee()
p=Programmer()
print(a.company,p.company)     
p.show()
p.printLanguage()
p.showLanguage()
