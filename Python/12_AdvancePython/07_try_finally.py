
try:
    a=int(input("Enter a Number: "))
    print(a) 


except Exception as e:  #default me error jitne trah ka hoga wo dekhega, but different trah k error per hum kuch alag messege dena chahe to
    print(e)            #invalid literal for int() with base 10: 'qwsd'

finally:    #ye kabhi b chalega pass pe bhi error per bhi
    print("I am inside finally")

print("print") #yaha agr ye print bhi likha jaye simple to dono case me run horha to finally q

#agr function ke andar finally banao to print ni karega finally dono case me run karega print run nhi hoga/@ return mtd
# ho ander to return k bad code execute nahi hota per finally karega rule break kar ke:

# def o():
#     try:
#         a=int(input("Enter a Number: "))
#         print(a) 
#         return


#     except Exception as e: 
#         print(e)
#         return           

#     finally:   
#         print("I am inside finally")

# o()
