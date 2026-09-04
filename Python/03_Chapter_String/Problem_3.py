sentence="i am a  boy."
print(sentence.find("  "))
#Find is used to get index,it does not give boolean it give result,here we have used to ensure double space is present or not

print("  " in sentence)
#It will give boolean output

print(sentence.index("  "))
#if it find then give the index and if not then give error it is the difference from "find"
 #ss