#Sum of natural number
def sum(n):
    if(n==1):
        return 1
    s=n+sum(n-1)
    return s
n=int(input("ENter number"))
print(sum(n))