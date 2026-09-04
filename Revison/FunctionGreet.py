#create a prog in which greet to the user with functions call:
def greet(name):
    print("Hi "+name+"How are you !!!!")
    print("Hi,",name,"How are you !!!!")
    print("Hi {} How are you !!!!".format(name))
    print(f"Hi {name} How are you !!!!")

name=input("Enter the name ")

#Function call:
greet(name)
