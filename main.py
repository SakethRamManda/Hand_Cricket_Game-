#Welcome to Hand Cricket Project
import random
def player_bat():
    while True:
        #aksing user to give an input in the range of 1 to 10
        user=int(input("enter number between 1 to 10 to bat:"))
        if(1<=user<=10):
            return user
        else:
            print("Invalid choice.Please make sure your choice lies in the range")
def player_bowl():
    while True:
        #aksing user to give an input in the range of 1 to 10
        user=int(input("enter number between 1 to 10 to bowl:"))
        if(1<=user<=10):
            return user
        else:
            #if user choose any option rather than 1 and 2
            print("Invalid choice.Please make sure your choice lies in the range")

def comp():
    #computer taking random inputs in the range 1 to 10
    return random.randint(1,10)
def user_bat():
    pscore=0
    pout=False
    Cout=False
    cscore=0
        #User will bat first
    print("You Will Bat first")
    while(not pout):
        #calling user choice 
        pchoice=player_bat()
        #calling computer choice
        Cchoice=comp()
        print(f"Your choice is {pchoice}")
        print(f"Computer choice is {Cchoice}")

      #checking if player choice and user choice is equal or not
        if(pchoice==Cchoice):
            print("You are Out!")
            pout=True
        else:
            #calculating the score of the user
            pscore=pscore+pchoice
            print(f"Your score={pscore}")
    print(f"Your score={pscore}")
    #Now Computer will bat!
    print("Computer will Bat!")
    while(not Cout):
        pchoice=player_bowl()
        Cchoice=comp()
        print(f"Computer Choice={Cchoice}")
        if(pchoice==Cchoice):
            #checking if player choice and user choice is equal or not
            print("Computer is Out!")
            Cout=True
            #checking if computer crossed the score the user or not
        elif(cscore>pscore):
            Cout=True
        else:
            #Calculating the score of the computer
            cscore=cscore+Cchoice
            #printing the score of the computer's score
            print(f"Computer Score={cscore}")
    print(f"Your score={pscore}")
    print(f"Computer score={cscore}")
  #checking who won the match
    if(pscore>cscore):
        print("Congratulations You won!")
    elif(cscore>pscore):
        print("Sorry! You lost the game")
    else:
        print("It's a Tie!")
def user_bowl():
    cscore=0
    Cout=False
    pout=False
    pscore=0
        #Now Computer will bat!
    print("Computer will Bat!")
    while(not Cout):
        pchoice=player_bowl()
        Cchoice=comp()
        print(f"Computer Choice is{Cchoice}")
        if(pchoice==Cchoice):
            #checking if player choice and user choice is equal or not
            print("Computer is Out!")
            Cout=True
            #checking if computer crossed the score the user or not
        else:
            #Calculating the score of the computer
            cscore=cscore+Cchoice
            print(f"Computer score is {cscore}")
    print(f"Computer score={cscore}")
    #User will bat
    print("You Will Bat")
    while(not pout):
        #calling user choice 
        pchoice=player_bat()
        #calling computer choice
        Cchoice=comp()
        print(f"Your choice is {pchoice}")
        print(f"Computer choice is {Cchoice}")

      #checking if player choice and user choice is equal or not
        if(pchoice==Cchoice):
            print("You are Out!")
            pout=True
        elif(cscore<pscore):
            pout=True
        else:
            #calculating the score of the user
            pscore=pscore+pchoice
            print(f"Your score is {pscore}")

        print(f"Your Score={pscore}")
       #printing the score of the computer's score
        print(f"Computer Score={cscore}")
  #checking who won the match
    if(cscore<pscore):
        print("Congratulations You won!")
    elif(cscore>pscore):
        print("Sorry! You lost the game")
    else:
        print("It's a Tie!")

def hand_cricket():
    toss=input("enter your choice 1:batting and 2:bowling")
    if(toss=="1"):
        user_bat()
    elif(toss=="2"):
        user_bowl()
    else:
        print("Invalid Input.Please check your input")
        hand_cricket()

    again=input("Do you want play again? Enter Y:Yes or N:No").lower()
    if(again=="y"):
        hand_cricket()
    elif(again=="n"):
        print("Thank you for playing.Hope you enjoyed the game")
    else:
        print("enter valid input")

#start game
if __name__=="__main__":
  hand_cricket()