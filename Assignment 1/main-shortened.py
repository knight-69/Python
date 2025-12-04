import random
'''
1 for snake
-1 for water
0 for gun

'''
computer =random.choice([-1,1,0])
youstr =input("Enter your choice :")
youDict ={"s" :1, "w":-1,"g" : 0}
reverseDict ={1:"snake", -1:"water",0:"gun"}
you =  youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")
if(computer == you):
    print("it is a draw")



else:

    '''
     if(computer == -1 and you ==1): (Computer -you )= -2
        print("You win!")

    elif(computer == -1 and you ==0): (Computer -you )= -1
        print("You Lose!")

    elif(computer == 1 and you ==-1): (Computer -you )= 2
        print("You Lose!")

    elif(computer == 1 and you ==0): (Computer -you )= 1
        print("You Win!")

    elif(computer == 0 and you ==-1): (Computer -you )= 1
        print("You win!")

    elif(computer == 0 and you ==1): (Computer -you )= -1
        print("You Lose!")

    the below logic is written on the basis of the value of computer - you

    ''' 
    if((computer - you) == -1 or (computer - you) ==2):
        print("you lose ")

    else:
        print("you win")