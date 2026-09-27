# Inheritance the adoption of method and variable from different class as we say Parent n child.
class Fruits:
    def __init__(self,name):
        self.name=name

    def display(self):
        print(f"Type of Fruits is {self.name}")

class Mango(Fruits)  :
    def __init__(self,name,type):
        super().__init__(name)
        self.type=type
        
    def mangoType(self):
        print(f"Type of mango is {self.type}")  

#object creation of parent class
f=Fruits("Mango")
f.display()
print(f.name)

#object creation of child class
m=Mango("mango","Alphanso",)
m.mangoType()
print(m.type)

m.display()
