from functools import reduce

#Map- run function for item together --for multiple vale

l=[1,2,3,5,8]
sq=lambda x:x*x
sqlist=map(sq,l)
print(list(sqlist))

#Filter. --for filter output
def even(n):
    if(n%2==0):
        return True
    return False
evenNum=filter(even,l)
print(list(evenNum))

#REDUCE------for one output
def sum(a,b):
    return a+b

mul=lambda x,y:x*y

redSum=reduce(sum,l)
print(redSum)

multiply=reduce(mul,l)
print(multiply)


