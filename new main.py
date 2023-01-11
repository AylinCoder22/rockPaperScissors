import random
#welcomes the user to the rock paper scissorts game
print("Welcome to the rock paper scissors game \n")

doYouPlay = input("Do you want to play?\n Yes or no: \n")
if doYouPlay == "Yes" or doYouPlay == "yes":
 #if typed "yes" than the program will let you continue
    print("LEYS PLAYYYY")
else: 
    print("bye")
        #if typed anything else the program stops
    exit()
#three options that the computer can use for the random function
options = ["rock","paper","scissors"]

#scores = 0 for both computer / player in the beggining
player_score = 0
computer_score = 0 


def game ():
#start of the loop

    while True:
        # the question 
        question1= input("TYPE : rock , paper , scissors or N to quit \n")

        if question1 == "N":
        #exits progam if you no longer want to continue
            print("byee")
            break 

        rand = random.randint(0,2)
        computerChoice = options[rand]
        print("computer picked:", computerChoice)

    #different options of what will happen during the game
        if computerChoice == question1:
            print("it's a draw")
        elif question1 == "rock" and computerChoice == "scissors":
            print("You won")
            player_score + 1
        elif question1 == "scissors" and computerChoice == "paper":
            player_score + 1
            print("you won!")
        elif question1 == "paper" and computerChoice == "rock":
            player_score + 1
            print("you Won!")
        else:
            computer_score + 1
            print("you lose!")  

    print(f"player total scores: {player_score}\nComputers total score:{computer_score}")
game()
