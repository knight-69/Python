import random

def game():
    print("You are playing the game..")
    score = random.randint(1,62)
    #fetch the hiscore
    with open("hiscore.text")as f:
        hiscore =f.read()
        ifhiscore = int(hiscore)

    print(f"your score:{score}")
    if(score>hiscore or hiscore==""):
        #write this hiscore to the file

    return score


game()