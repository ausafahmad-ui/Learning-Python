class Employee:
    name="Ausaf"
    pin=865466
    def intro(self):
        print(f"{self.name} belongs to pin {self.pin}")
    @staticmethod               #it does not require self,it stict to the class where it is created
    def staticmtd():
        print("Hello Tester, hows ur coding going!!!!")
    def __init__(self):         #It will call many time as creation of object of its class
        print("It is dunder mether bcz it containg two underscore !")
e=Employee()
e.intro()
e.staticmtd()
e2=Employee()            