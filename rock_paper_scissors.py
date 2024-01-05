import random

player_choice = input("Choose wise [r]ock - [p]aper - [s]cissors")
player_move = ""

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

if player_choice == "r":
    player_move = rock
elif player_choice == "p":
    player_move = paper
elif player_choice == "s":
    player_move = scissors
else:
    raise SystemExit("Please try again, your input was not valid")

print(f"Player choose {player_move}")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = scissors
elif computer_random_number == 3:
    computer_move = paper

print(f"Computer choose {computer_move}")

if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move ==  scissors and computer_move == paper):
    print("You win!")
elif (player_move == rock and computer_move == rock) or \
        (player_move == paper and computer_move == paper) or \
        (player_move == scissors and computer_move == scissors):
    print("Draw!")
else:
    print("You loose!")


