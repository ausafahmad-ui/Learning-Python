#Open() is built-function which take two argument-("File Path","r or w" or"a" or "+") --by default is is always "r"

f=open("File.txt") #isliye yha "r" nahi likha
data=f.read()
print(data)
f.close()
