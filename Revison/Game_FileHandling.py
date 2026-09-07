import random
#NOTE: Save the high score to file

score=random.randint(1,100)
with open("HighScore.txt","r") as r:
    highScore=r.read()
    if(highScore != ""):
        highScore=int(highScore)
    else:
        highScore=0    
print(f"Your highest score is {score} and the previous score was {highScore}")
if(score>highScore):
    with open("HighScore.txt","w") as w:
        w.write(str(score))
