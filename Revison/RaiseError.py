
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
if b==0:
    raise ZeroDivisionError("deno cant be zero")
else:
    print(a / b)

