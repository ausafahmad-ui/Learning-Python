class Employee:
    a=1
    def __init__(self):
        print(f"constructor of Employee")

class Coder(Employee):
    b=2
    def __init__(self):
        print(f"constructor of coder")
        super().__init__ ()   

class Programmer(Coder):
   c=3
   def __init__(self):
        print(f"constructor of Programmer")
        super().__init__()

a=Employee()
print(a.a)

b=Coder()
print(b.a,b.b)

c=Programmer()
print(b.a,b.b,c.c)
