# Append will add the things in the existing files at the end
text="I am Tester"
with open("File.txt","a") as f:
    f.write(text)

with open("File.txt","r") as i:  
    print(i.read())    