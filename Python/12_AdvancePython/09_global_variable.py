a=89 #global hai
def fun():
    # global a  #per yha global ko mtd k ander access de diya to global 9 hoga # 9
    a=9
    print(a)
fun()   #9 mtd wala
print(a)  # global wala  

  