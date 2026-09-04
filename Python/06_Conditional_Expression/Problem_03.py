# Find the spam messeges
s1="Make a lot of money"
s2="Buy now"
s3="Subscribe this"
s4="Click this"

Messege =input("Enter you messege! ")
formatMsg=Messege.lower()

if(s1.lower() in formatMsg):
    print("This is spam")
elif(s2.lower() in formatMsg):
    print("This is spam")
elif(s3.lower() in formatMsg):
    print("This is spam")
elif(s4.lower() in formatMsg):
    print("This is spam")   
else:
    print("NO SPAM")    