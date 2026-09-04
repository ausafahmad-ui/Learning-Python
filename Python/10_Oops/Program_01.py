#NOTE:store the information of programmer working in microsoft
class Programmer :
    company="Microsoft"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

a=Programmer("Ausaf")
print(a.name,a.salary,a.company)
b=Programmer("Suchit",80000)
print(b.name,b.salary,b.company)
