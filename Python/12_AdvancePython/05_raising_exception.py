a=int(input("Enter Number"))
b=int(input("Enter Number"))

#it is for developer to know the reason of crash application if he is doing wrong kind of this in future debugging
if(b==0):
    raise ZeroDivisionError("Not supported by python that you divide by zero")


print(f"divison of a and b {a/b}")
