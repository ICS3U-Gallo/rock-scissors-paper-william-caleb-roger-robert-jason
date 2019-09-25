 
 
import random

# Name: William

game_number = 1
player_score = 0
computer_score = 0

while True:
    print("----- Game " + str(game_number) + " ----------------------------------")

    # Check if the player inputs the correct value, such as R, P, S or Q.
    # If not, keep on asking the player to input the correct value.
    while True:
        print("Input R for Rock, P for Paper and S for Scissor. Input Q to quit the game.")
        player_choice = input("Your Choice: ")

        if player_choice.upper() in ["R", "P", "S", "Q"]:
            break

    # Quit the game if the player decides to quit.
    if player_choice.upper() == "Q":
        break

    # Display player's choice.
    if player_choice == "R":
        print("Your Choice is Rock.")
    elif player_choice == "P":
        print("Your Choice is Paper.")
    elif player_choice == "S":
        print("Your Choice is Scissor.")

    number = random.randint(1, 3)

    # For computer choice:
    # 1 is Rock
    # 2 is Paper
    # 3 is Scissor

    computer_choice = ""

    # Assign computer's choice based on the randomized number.
    if number == 1:
        computer_choice = "R"
        print("Computer's Choice is Rock.")
    elif number == 2:
        computer_choice = "P"
        print("Computer's Choice is Paper.")
    elif number == 3:
        computer_choice = "S"
        print("Computer's Choice is Scissor.")

    # Compare player's choice with computer's choice.
    if player_choice.upper() == "R":
        if computer_choice == "R":
            print("Tie!")
        elif computer_choice == "P":
            print("You Lose!")
            computer_score = computer_score + 1
        elif computer_choice == "S":
            print("You Win!")
            player_score = player_score + 1

    elif player_choice.upper() == "P":
        if computer_choice == "R":
            print("You Win!")
            player_score = player_score + 1
        elif computer_choice == "P":
            print("Tie!")
        elif computer_choice == "S":
            print("You Lose!")
            computer_score = computer_score + 1

    elif player_choice.upper() == "S":
        if computer_choice == "R":
            print("You Lose!")
            computer_score = computer_score + 1
        elif computer_choice == "P":
            print("You Win!")
        elif computer_choice == "S":
            print("Tie!")
            player_score = player_score + 1

    game_number = game_number + 1

# Announcing Result.
print("----- Result Summary --------------")
print("Player's Score is " + str(player_score))
print("Computer's Score is " + str(computer_score))

if player_score > computer_score:
    print("You have won this Rock-Paper-Scissors Game!")
elif player_score < computer_score:
    print("You have lost this Rock-Paper-Scissors Game!")
else:
    print("The Game is tied!")


