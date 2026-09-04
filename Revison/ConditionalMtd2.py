marks=int(input("Enter your age before proceeding!: "))
if marks<14 and marks > 0 :
    print("You are too young you cant do it")
elif marks >= 14 and marks <=35 :
    print("You are eligible for filling the govt service form")
elif marks>100:
    print("You are not Human !")          
else:
    print("Sorry! You are overage, you cant fill the form")
