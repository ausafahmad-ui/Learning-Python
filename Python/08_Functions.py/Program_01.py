#Using function find the greates number

def greatest(a,b,c):
    if(a>b and a>c):
       return a
    elif(b>a and b>c):
        return b 
    elif(c>a and c>b):
        return c   

gretestNum=greatest(2,40,9)    
print("greatest number is:",gretestNum)