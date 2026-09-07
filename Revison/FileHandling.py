'''
| Mode  | Meaning                                       |
| ----- | --------------------------------------------- |
| `"w"` | Overwrites existing content                   |
| `"a"` | Adds new content without deleting old content |
| `"r"` | Reads the file                                |
'''
w=open("Hareem.txt",'a')
# data=w.write("My third  home is at chandpali")
w.close()

a=open("Hareem.txt",'a')
data=a.write("\nMy third  home is at chandpali")
a.close()

f=open("Hareem.txt",'r')
data=f.readlines()
print(data)
f.close()