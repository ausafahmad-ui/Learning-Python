class Employee:
    name="Ausaf"
    pin=123123  
    def getInfo(self):
        print(f"This is {self.name} whose pin is {self.pin}")  #it can be anything self/asdf/kuch b
    def greet(self):
        print("Good Morning")
asf=Employee()
asf.name="rohan" #Object/instance-attribute which take more priority then class attribute
print(asf.name,asf.pin)
asf.getInfo()   # it actually converting into Employee.getInfo(asf)-->we are passing object name a'asf" in argument of functionn so it is not accepting
asf.greet()