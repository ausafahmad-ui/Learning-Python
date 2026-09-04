# Find the word in the sentences
sentence="Hey this Ausaf! i am automation tester and wanna become sdet"
word=input("Enter you name to check whether the talk about you or not: ")
if(word.lower() in sentence.lower()):
    print("Yes they are talking about you")
else:
    print("No they talking something about other")    