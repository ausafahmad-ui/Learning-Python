import random

'''
paper=0
stone=1
scissor=-1
'''


# player_input= input("Enter your choice: ")
dictionary={"paper":0,"stone":1,"scissor":-1}
game=True
while(game):
    n=True
    while(n):
        player_input= input("Enter your choice: ")
        
        if player_input.lower() in dictionary:
            playerchoice=dictionary[str(player_input.strip().lower())]
            n=False
        else:
            print("Wrong Input! Try Again")
            n=True
    

    systemDictionary={0:"paper",1:"stone",-1:"scissor"}
    systemChoice=random.choice(list(systemDictionary.keys()))
   
    if(playerchoice==systemChoice):
        print(" Match Draw")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
        
    elif(playerchoice==0) or (systemChoice==1) :
        print(" You WON !!!! woohhhhh")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
    elif(playerchoice==0) or (systemChoice==-1) :
        print(" You Looose")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
    elif(playerchoice==1) or (systemChoice==0) :
        print(" You Looose")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
        print(" You WON !!!! woohhhhh")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
    elif(playerchoice==1) or (systemChoice==-1) :
        print(" You WON !!!! woohhhhh")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
    elif(playerchoice==-1) or (systemChoice==1) :
        print(" You Looose")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
    elif(playerchoice==-1) or (systemChoice==0) :
        print(" You WON !!!! woohhhhh")
        print(f"Your input is {player_input.lower()} and System choice is {systemDictionary[systemChoice]}")
    action=input("want to play again if yes then type YES or for exit type NO:" )  
    if(action.strip().lower()=="yes"):
        game=True
    else:
        game=False
        print(" Game Over")