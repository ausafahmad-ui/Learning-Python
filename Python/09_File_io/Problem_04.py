word="Donkey"
word=word.lower()
with open("Don.txt","r") as f:
    text=f.read()
    

newText=text.replace(word,"####")

with open("Don.txt","w") as f:
    text=f.write(newText)