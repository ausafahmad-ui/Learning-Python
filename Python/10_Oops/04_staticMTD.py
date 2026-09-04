class Employee:
    name="Ausaf"
    pin=123123  
    def getInfo(self):
        print(f"This is {self.name} whose pin is {self.pin}")  

    @staticmethod    #it does not take object refarance
    def greet():
        print("Good Morning")
asf=Employee()
asf.name="rohan" 
print(asf.name,asf.pin)
asf.getInfo()   
asf.greet()