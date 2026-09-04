#NOTE: Readlines()/Readline()

f= open("MyFile.txt","r")
lines=f.readlines()  #It give each line as item of list[]
print(lines,type(lines))
f.close()



# lines1=f.readline()
# print(lines1,type(lines1))


# lines2=f.readline()
# print(lines2,type(lines2))


# lines3=f.readline()
# print(lines3,type(lines3))

#LOOP
# line=f.readline() #first line read kiya-->condition created for while loop also to start and terminate
# while(line !=""):   #agar line empty nahi hai to ander jao loop mein
#     print(line) #print kiya first line
#     line=f.readline()   #yaha next line read kiya ,next hai to read krk rakh lega
# f.close()