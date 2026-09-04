# Read the poem and find poem have word"twinkle"
with open("Poem.txt","r") as f:
    data=f.read()

if("Twinkle" in data):
    print("Yes it is present")    
else:
    print("Not found")    