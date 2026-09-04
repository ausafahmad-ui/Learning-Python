class Employee:
    company="Ethara"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}") 

# class Programmer:
#     company="Kubera"
#     def show():
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")
#     def showLanguage():
#         print(f"The name of the employee is {self.name} and his/her language is {self.language}")


class Programmer(Employee):
    company="Kubera"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
a=Employee()
b=Programmer()
print(a.company,b.company,b.show())            