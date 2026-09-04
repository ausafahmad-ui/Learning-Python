# save in the file table
n=int(input("enter number"))
table=[n*i for i in range(1,11)]
with open("Table.txt","a") as f:
    f.write(str(table)+"\n")