class Employee:
    a=1
 
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")


    #PROPERTY GETTER AND SETTER SETTER HAI/ Humne e.name ko isme get kiya fir use toda fnam or lname mein bina user k jan kari mein 
    #example of ABSTRACTION-->user lname fname call pe de rhe hai per kaise ye hum jante hai
    @property
    def name(self):
        return f"{self.fname}-{self.lname}"
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=Employee()
print(e.a) #its normal class atribute
e.show()  
e.name="Ausaf khan" # value
print(e.name) #by use of property so we can call as attribute
print(e.fname)
