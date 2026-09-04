#NOTE:Create class Train and functions of trains,ticket and fare
import random
class Train:
    
    # def __init__(self): it will not work bcz python execute the last creation and also second one is constructor
    #     print("Plan your Journey")

    def __init__(self,trainNum,frm,to):
        self.trainNum=trainNum
        self.frm=frm
        self.to=to
        
    def bookTicket(self):
        print(f"Train is booked from {self.frm} to {self.to} in the {self.trainNum}!")

    def ticketAvailable(self):
        print(f"Available seats for {self.frm} to {self.to} is {random.randint(0,72)} ")    

    def ticketFare(self):
        print(f"Booking of journey {self.frm} to {self.to} is {random.randint(200,999)} Rupees(dynamic fare)")
print("Plan your journey! ")
train=int(input("Train number "))
origin=input("Origin place ")
dest=input("destination place ")


s1=Train(train,origin,dest)
s1.bookTicket()
s1.ticketAvailable()
s1.ticketFare()
