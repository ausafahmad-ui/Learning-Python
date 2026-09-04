name=input("Enter you name: ")
date=input("Enter the date: ")

letter=f'''Dear {name}\nYou are selected!\nDate {date}'''
print(letter)
#Here it is taking input and printing in format

Template='''..Dear <|Name|>
            You are Selected!..
            <|Date|>'''
print(Template.replace("<|Name|>","Ausaf").replace("<|Date|>","15th Aug 2100"))
#NOTE: Here, first name will get replace n give output in string of complete sentence and again replace date from the preoutput string
