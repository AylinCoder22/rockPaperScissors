import random
print("Welcome to the rock paper scissors game \n")

def Wantoplay():
    doYouPlay = input("Do you want to play?\n Yes or no: \n")
    if doYouPlay == "Yes" or doYouPlay == "yes":
        print("LEYS PLAYYYY")
    else: 
        print("bye")
        exit()
Wantoplay()

options = ["rock","paper","scissors"]

def game ():

    question1= input("type : ROCK , PAPER , SCISSORS or type N to quit\n")
    
    if question1 == "N":
        print("byeee!")
        exit()

    rand = random.randint(0,2)
    computerChoice = options[rand]
    print("computer picked:", computerChoice)

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