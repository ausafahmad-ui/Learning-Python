
# DICTIONRY-it is always comes in curly braces and in key-pair,and ypu can print it with key refarence and its type very fast
# serch very fast
marks={"Ausaf":100,
       "adeeb":90,
       "harim":101
       }
print(marks)
print(marks,type(marks))
print(marks,type(marks),type("Ausaf"))

# print(marks[1]) it does not run on index ,it work on keys
print(marks["Ausaf"])


student = {
    "name": "ausaf",
    "age": 24
}
print(student.items())
for key, value in student.items():
    print()

