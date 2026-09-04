list=["gzd", "lala", "bc"]
with open("MultipleWords.txt","r") as f:
   text=f.read()

for word in list:
   text=text.replace(word,"dogla")

with open("MultipleWords.txt","w") as f:
   f.write(text)


Testing@dev123