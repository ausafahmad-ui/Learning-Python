#NOTE:entered number is prime or not
number=int(input("Enter number: "))

for n in range(2,int(number/2)+1):
    if(number%n==0):
        print("not prime")
        break
else:
    print("it is prime")    