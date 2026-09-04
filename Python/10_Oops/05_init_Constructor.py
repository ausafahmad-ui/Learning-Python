class Employee:
    name="Ausaf"
    pin=123123  
    def getInfo(self):
        print(f"This is {self.name} whose pin is {self.pin}")  

    @staticmethod    #it does not req object refarance,it will execute on call without passing object refrance unlike "asf"
    def greet():
        print("Good Morning")

    def __init__(self):  #it is special mtd called DUNDER mtd,which execute while creating object.Only __init__
        print("I am creating object")


asf=Employee()
asf.name="rohan" #instance attributes
print(asf.name,asf.pin)
asf.getInfo()   
asf.greet()
asf1=Employee() #self executed again on object creation