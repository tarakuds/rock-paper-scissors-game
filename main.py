import random

print("Welcome to the Rock, Paper, Scissors game. All the best as you play with the computer. May the Force be with you.")
print("These are the rules Of the game, R = Rock, P = Paper, S = Scissors. You can only make one choice.")
choices = ["R", "P", "S"]

computer = random.choice(choices)
player = None
tie = "There is a tie"
win = "YOU WIN"
lose =  "You LOSE"
# if choices = "R";
#     value = "Rock"

while player not in choices:
    print("Wrong, you have to make a valid response. These are the rules Of the game, R = Rock, P = Paper, S = Scissors. You can only make one choice.")
    player = input("What do you choose? R,P or S :- ").upper()

print("Player - ", player, "CPU - ", computer)
if player == computer:
    print(tie)
    retry = input("Will You like to play again? Yes / No ? ").lower()
    if retry == "yes":
        player = input("What do you choose? R,P or S :- ").upper()
        ######################
        if player == computer:
            print(tie)
            retry = input("Will You like to play again? Yes / No ? ").lower()
        elif retry == "no":
            player = input("Thank you")
        ########################
    elif retry == "no":
        print('Thank you')

elif player == "R":
    if computer == "S":
        print(win)
    if computer == "P":
        print(lose)
elif player == "S":
    if computer == "P":
        print(win)
    if computer == "R":
        print(lose)
elif player == "P":
    if computer == "R":
        print(win)
    if computer == "S":
        print(lose)


