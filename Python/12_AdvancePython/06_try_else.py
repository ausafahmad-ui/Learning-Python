
try:
    a=int(input("Enter a Number: "))
    print(a) 


except Exception as e:  #default me error jitne trah ka hoga wo dekhega, but different trah k error per hum kuch alag messege dena chahe to
    print(e)            #invalid literal for int() with base 10: 'qwsd'

else:       #Else tabhi chalega jb try successfully run hoga agar except me gya to nahi hoga
    print("i am inside else")
