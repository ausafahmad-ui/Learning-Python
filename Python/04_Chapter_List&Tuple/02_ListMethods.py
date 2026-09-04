
#list methods are approx same as string methods
friends=["Apple","Orange",5,345.98,False,"akash"]
print(friends)#same refrane call
#---------append()--------------
friends.append("khan")# add krta hai by default at the end--action performed
#NOTE print(friends.append("khan")) iska matlab mutable me action hote wakt print krna sahi ni hai,qk wha sirf action ho rha koi new object nahi ban rha.
print(friends) #same refrnce with change call hoga by created refrance

#---------sort()--------------
l1=[1,9,4,7]
# print(l1.sort()) # nhi karega kaam kyu ke sort() return kuch nhi karta hai isliye NONE hoga print
result=l1.sort() #result mein bhi NONE value jayega jisse print NONE hoga
#sort actually arrange here the list only,no output or new object creation,so for output we have to print the refrance and we know list are mutable
print(l1)

# list.sort() → changes the existing list → returns None
# sorted(list) → creates and returns a new sorted list


#---------reverse()--------------

l1.reverse()
print(l1)


#---------insert()--------------
#nsert is used to add anywhere with index 
l1.insert(3,3333)
print(l1)

#-------Pop------------------
l2=[1,9,4,7]
l2.pop(0)# provided index will be remove
print(l2.pop(0))
print(l2)