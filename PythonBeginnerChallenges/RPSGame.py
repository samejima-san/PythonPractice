import random


#rock paper scissors game, greets player and gives messages
#after you've won or lost

def getCompInput():
    randnum = random.randint(1,4)
    if randnum == 1:
        return "paper"
    elif randnum == 2:
        return "rock"
    else:
        return "scissors"
points = 0
cpoints = 0
i = False
while i == False:
    compInput = getCompInput() 
    userInput = input("rock, papers scissors?\n").lower()
    if userInput == "rock" or userInput == "paper" or userInput == "scissors":
        if userInput == "rock" and compInput == "scissors":
            points += 1
            print("Rock beats scissors! Player wins!")
        elif userInput ==  "scissors" and compInput == "paper":
            points += 1
            print("Scissors beats paper! Player wins!")
        elif userInput ==  "paper" and compInput == "rock":
            points += 1
            print("Paper beats rock! Player wins!")
        elif compInput == "rock" and userInput == "scissors":
            cpoints += 1
            print("Rock beats scissors! Computer wins!")
        elif compInput ==  "scissors" and userInput == "paper":
            cpoints += 1
            print("Scissors beats paper! Computer wins!")
        elif compInput ==  "paper" and userInput == "rock":
            cpoints += 1
            print("Paper beats rock! Computer wins!")
        else:
            print("Tie")
    else:
        print("silly you, you misspelled rock paper or scissors.")
    print("\nPlayer Wins: " + str(points))
    print("Computer Wins: " + str(cpoints))
    print("")