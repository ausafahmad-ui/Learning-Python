
''' | Feature          | List      | Tuple     | Set           | Dictionary                      |
    | ---------------- | --------- | --------- | ------------- | ------------------------------- |
    | Syntax           | `[]`      | `()`      | `{}`          | `{key:value}`                   |
    | Ordered          | ✅ Yes     | ✅ Yes     | ❌ No          | ✅ Yes                        |
    | Mutable          | ✅ Yes     | ❌ No      | ✅ Yes         | ✅ Yes                        |
    | Duplicate values | ✅ Allowed | ✅ Allowed | ❌ Not allowed | ❌ Duplicate keys not allowed |
    | Indexing         | ✅ Yes     | ✅ Yes     | ❌ No          | ❌ Uses keys                  |
    | Key-value pair   | ❌ No      | ❌ No      | ❌ No          | ✅ Yes                        |
    | Fast searching   | Medium    | Medium    | Fast          | Very fast                       |'''




# Set and Dictionary both are created with curly braces, so for creating empty we have to be alert while set and dictionary with element is okay
# dictionary have key-pair and set have invidual elements

d={} #empty dictionary
print(type(d))

s=set()     #it does not allow duplicates, does not maintain order
print(type(s)) #empty set ! dont use s={} for empty set


ss={5,5,5,5}
print(ss)
print(type(ss))

sss={5,1,90,3,55}
print(sss)
print(type(sss))# accidently or luckily its maintaing here but it is never sure ,it doesnt allow duplicacy

f = {"banana", "apple", "cat", "dog"}
print(type(f))        # it is not maintaning here





