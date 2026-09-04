try:
    a=int(input("enter number"))
    b=int(input("enter number"))
    print(a/b)

except ZeroDivisionError as e:
    print("infinite error")