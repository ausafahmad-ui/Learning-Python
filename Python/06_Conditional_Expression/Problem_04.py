# verify the username is less than 10 char
username=input("Enter your username: ")
if(len(username)<10):
    print("Yes less than 10")
else:
    print("Exceeded")
