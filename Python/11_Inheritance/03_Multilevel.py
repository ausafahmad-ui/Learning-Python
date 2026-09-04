class Employee:
    a=1
class Coder(Employee):
    b=2
class Programmer(Coder):
   c=3

a=Employee()
print(a.a)  #attribute of employee can be access on object of Employee
# print(a.b)  #attribute of Code is not accessible on object of Employee

b=Coder()
print(b.a,b.b) #can be access both inherited the employee to coder

c=Programmer()
print(c.a,c.b,c.c)
