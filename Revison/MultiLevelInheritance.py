class Ausaf:
    a=1
    def __init__(self,name):
        self.name=name
    def job(self):
        print("Job")

class Sufiya(Ausaf):
    a=3
    def __init__(self,Add,name):
            self.Add=Add
            super().__init__(name)
    def job(self):
        print("HouseMaker")     

class Hareem(Sufiya): #jo class pahle hoga uska call hoga agr iske pass khud k method ya variable ni hai to
    def job(self):
        print("Study")
    # pass
s=Sufiya("hathua","Gopal")
print(s.name,s.Add)