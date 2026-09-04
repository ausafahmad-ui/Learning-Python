marks={"Ausaf":100,
       "adeeb":90,
       "harim":101
       }

# Dictionary k items ko as tuple ke liye hum isko list mein get kr skte hai, jo iterate kar skte loop se
print(marks.items()) #
print(marks.keys())
print(marks.values())
print(marks)

marks.update({"srk":90,"shivika":89})
print(marks)

print(marks.get("Ausaf")) 
print(marks["Ausaf"])
print(marks.get("Ausaf2")) #return none if wrong keys
# print(marks["Ausaf2"]) #return error if wrong input
#  Dictionary is mutable
marks.pop("adeeb")# remove the given one
print(marks)
marks.update({"alina":102}) # add in the last
print(marks)
marks.popitem()# remove the last one
print(marks) 