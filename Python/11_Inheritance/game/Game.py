#NOTE:Quize get random number from pc and guess by hinting by pc till it get same
import random
n=random.randint(1,100)

a=-1
guesses=0
while(a!=n):
    a=int(input("Enter your number: "))
    if(a<n):
        print("Lower then guessed number.Enter higher number: ")
    else:
         print("Greater then guessed number.Enter Lower number: ")    
    guesses=guesses+1
print(f"you have guessed the correct number-: {n} and took times-: {guesses}")          