#set are un-ordered
#you can access by index
#it is un-index
#it does not allow duplicates

name={1,4.5,8,90,"Ausaf"}
print(name,type(name))
name.add("istyk")
print(name)
print(len(name)) #work in set,list,tuple,dictionary

name.remove(1)
print(name,type(name))

print(name.pop())
print(name,type(name))

s1={1,145,146}
s2={7,8,1,78}
print(s1.union(s2)) #dono ke item ek sath dekhayega
print(s1.intersection(s2)) # common element deta hai