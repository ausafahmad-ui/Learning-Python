# f=open("File.txt") #isliye yha "r" nahi likha
# data=f.read()
# print(data)
# f.close()
#--------same as above only it closes file automatically after executing block---------/\/\/\/\/\/
with open("File.txt","r") as f:
    print(f.read())