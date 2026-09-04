class Employee:
    name="Ausaf" #class-attribute
    pin=123123  #class-attribute
    

asf=Employee()
asf.name="rohan" #Object/instance-attribute which take more priority then class attribute
print(asf.name,asf.pin)