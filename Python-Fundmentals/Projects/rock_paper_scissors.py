import random

# Read player's Move
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

# Match player's move w/ possible answer
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemError("Invalid input. Try again!")

# Choose computer's move
computer_choice = random.randint(1, 3)
computer_move = ""

if computer_choice == 1:
    computer_move = rock
elif computer_choice == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose {computer_move}.")

# Check and write result
if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")