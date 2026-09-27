try:
    a=int(input("Type your number"))
except Exception as e:
    print(e)    
print("thankyou")    #try except smooth deal krega ar poora code run hoga
#yhi chij aise hoga to error per code ruk jayega


a=int(input("Type your number"))
print("thankyou") #ye run ni hoga try except hai ni to yhi fat gya code


try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))

    print(a / b)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

print("thanks")