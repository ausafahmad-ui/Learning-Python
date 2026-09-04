
try:
    a=int(input("Enter a Number: "))
    print(a) #user entered str it will give error so handing it with try catch

except KeyboardInterrupt as v:  #to direct type of error k sath print hoga yha
    print(v)

except Exception as e:  #default me error jitne trah ka hoga wo dekhega, but different trah k error per hum kuch alag messege dena chahe to
    print(e)            #invalid literal for int() with base 10: 'qwsd'

print("Thankyou")
