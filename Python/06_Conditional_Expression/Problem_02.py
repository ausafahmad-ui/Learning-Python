# Over all 40% and in each subject 33% required to pass 
marks=[]
s1=int(input("Enter marks "))
marks.append(s1)
s2=int(input("Enter marks "))
marks.append(s2)
s3=int(input("Enter marks "))
marks.append(s3)
percent_marks1=(sum(marks)/300)*100
if(percent_marks1>40 and (s1/100)*100>33 and (s2/100)*100>33 and (s1/100)*100>33):
    print("You are Pass and you obatain total: ",sum(marks))
else:
    print("Oho! You are fail,Better luck next time!","Obatained total: ",sum(marks))    

