#Argument with function 
# NOTE Type of functions----
# 1.Built in-->print(),Sum(),etc
# 2. User define functions

def greet(name="ADIL",ending="NAMASTEY"):
    print(f"""Hello ! To kaise hai aplog.Specially you {name}""")
    print(ending)
greet()
greet("bhaijan","Asslam!")
print("-----------------------------------------------")

def greet(name,ending):
    print(f"""Hello ! To kaise hai aplog.Specially you {name}""")
    print(ending)
greet("ausaf","bye bye") #CALL with user argument 
# greet() #give error
print("-----------------------------------------------")


def greet(ending,name="shalu"): 
    print(f"""Hello ! To kaise hai aplog.Specially you {name}""")
    print(ending)
greet("thankyou") # YAHA DEFAULT aur user based call ho skta hai but default bad me likho ar user define pahle at function definition per

greet("thankyou","Jaan")
print("-----------------------------------------------")