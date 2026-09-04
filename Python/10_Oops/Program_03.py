#NOTE:Does class attribute change after creating object attribute with same name(like static and non static in java)

class Demo:
    a=4
s=Demo()
print(s.a)
s.a=0
print(s.a)
print(Demo.a)
# No changes or alterations happened between clas and object attributes 
