class Ausaf:
    a=1
    def job(self):
        print("Job")

class Sufiya:
    a=3
    def job(self):
        print("HouseMaker")     

class Hareem(Sufiya,Ausaf): #jo class pahle hoga uska call hoga agr iske pass khud k method ya variable ni hai to
    def job(self):
        print("Study")
    # pass

h=Hareem()
h.job()
# h.a=2
print(h.a)