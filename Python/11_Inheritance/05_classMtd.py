class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")



e=Employee()
print(e.a) #its normal class atribute
e.show()    #its normal mtd of Employee
e.a=45  #obj refrance change class attribute value which always at high priority
#after creatinf mtd with claasmethod it will call class attribute not the object refrance value
print(e.a)
e.show()

