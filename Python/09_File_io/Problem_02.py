#save high score in file and save the highest one
import random

def game():
    print("Game start..")
    score=random.randint(1,100)
    with open("HighScore.txt","r") as h:
        hiscore=h.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0    
    print(f"Your high score is :{score}")

    if(score>hiscore):
        with open("HighScore.txt","w") as w:
            w.write(str(score))
    return score

game()