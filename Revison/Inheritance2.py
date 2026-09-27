class Vehicle:
    
    def engine(self):
        self.name=0
        print(self.name)

class Evehicle(Vehicle):
    def display(self):
        print(self.name)

e=Evehicle()
e.name="Four-stroke"

e.display()
e.engine()
p=Vehicle()
p.name="sss"
p.engine()