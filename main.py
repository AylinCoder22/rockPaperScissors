import random
#welcomes the user to the rock paper scissorts game
print("Welcome to the rock paper scissors game \n")

def Wantoplay():
#a function that asks the user if they want to continue the game 
    doYouPlay = input("Do you want to play?\n Yes or no: \n")
    if doYouPlay == "Yes" or doYouPlay == "yes":
        #if typed "yes" than the program will let you continue
        print("LEYS PLAYYYY")
    else: 
        print("bye")
        #if typed anything else the program stops
        exit()
Wantoplay()
#three options that the computer can use for the random function
options = ["rock","paper","scissors"]

def game ():
#question pick either rock paper scissors or type N to quit 
    question1= input("type : ROCK , PAPER , SCISSORS or type N to quit\n")

    if question1 == "N":
        #exits progam if you no longer want to continue
        print("byeee!")
        exit()

    rand = random.randint(0,2)
    computerChoice = options[rand]
    print("computer picked:", computerChoice)
#different options of what will happen during the game
    if computerChoice == question1:
        print("it's a draw")
    elif question1 == "rock" and computerChoice == "scissors":
        print("You won")
    elif question1 == "scissors" and computerChoice == "paper":
        print("you won!")
    elif question1 == "paper" and computerChoice == "rock":
        print("you Won!")
    else:
        print("you lose!")
game()
