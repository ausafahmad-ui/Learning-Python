# NOTE:::multiple text to store value,actually it create new object refrance and replace the old one,while in java it is not possible
name="Ausaf";

print(name.startswith('A'))
print(name.startswith('a')) #sensative
print(name.endswith('f'))
print(name.capitalize())

# Most used String Functions
text="hello world"
# CHANGE CASE:
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())

# REMOVE SPACE
print(text.strip())
print(text.rstrip())
print(text.lstrip())

# FIND AND REPLACE
text="i like java"
# new=text.replace("java","python")
print(text.replace("java","python"))
# print(new)
# print(new.find("python")) #give the index

#SPLIT & JOIN
Fruit="apple,baba"
print(Fruit.split(",")) #split return in List


alphbates="a","b","c"
n="-".join(alphbates)
alpha=['1','2','3']
num="-".join(alpha)
print(n)
print(num)

# Check Content
content="sophie"
print(content.isalpha())
print(content.isnumeric())
print(content.isdecimal())
print(content.istitle())
print(content.startswith('s'))
print(content.endswith("e"))

#Count & Length
phrase="Ausaf"
print(phrase.count('u'))
print(len(phrase))


# String Formatting
name="shahrukh"
profession='actor'
text1=f"he is {name} the great {profession}"
print(text1)
print("he is ",name ,"the great",profession)

# Reverse String
string="python"
print(string[::-1])# mean start:end:step of reading like if 1 then every step like 0,1,2,3,if 2 then it will run like 0,2,4,6
# minus mean run reverse way and positive mean run ahead way
print(string[0:6:2])
