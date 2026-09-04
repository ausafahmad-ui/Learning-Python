import random
'''
snake-water=snake wins
gun-water= water wins
water-snake=snake wins
gun-snake=gun wins
snake-gun=gun wins
water-gun=water wins

snake=1
gun=0
water=-1
'''
computer=random.choice([1,-1,0])
dictionarybackend={"1":"snake","-1":"water","0":"gun"}
dictionary={"snake":1,"water":-1,"gun":0}
user=input("Enter snake,water and gun: ").strip().lower()
if(user in dictionary):
    userchoice=dictionary[user] #In python dictionary(user) is not possible because () use to call function so for dict to get use sq bracket[]
else: 
    print("Wrong input") 
    exit()


if(userchoice==computer):
    print("Its Draw")   
    print(f"computer chose {dictionarybackend[str(computer)]}\nand you chose {user}")
else:
    if(userchoice==1 and computer==-1):
        print("You Win")
        print(f"computer chose {dictionarybackend[str(computer)]} \nand you chose {user}")
    elif(userchoice==1 and computer==0):
        print("You Loose")      
        print(f"computer chose {dictionarybackend[str(computer)]} \nand you chose {user}")
    elif(userchoice==0 and computer==1):
        print("You Win")
        print(f"computer chose {dictionarybackend[str(computer)]} \nand you chose {user}")
    elif(userchoice==0 and computer==-1):
        print("You Loose")      
        print(f"computer chose {dictionarybackend[str(computer)]} \nand you chose {user}")
    elif(userchoice==-1 and computer==1):
        print("You Loose")
        print(f"computer chose {dictionarybackend[str(computer)]} \nand you chose {user}")
    elif(userchoice==-1 and computer==0):
        print("You Win")    
        print(f"computer chose {dictionarybackend[str(computer)]} \nand you chose {user}")
    else:
        print("Something went wrong")      