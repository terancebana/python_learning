import random

choices = ["rock", "paper", "scissors"]

my_choice = int(input("What do you choose? O for Rock, 1 for Paper or 2 or Scissors.\n"))
my_string_choice = choices[my_choice]
machine_choice = random.choice(choices)

if my_string_choice == machine_choice:
    print("It\' a draw!")
elif my_string_choice == "rock" and machine_choice == "scissors" or my_string_choice == "paper" and machine_choice == "rock" or my_string_choice == "scissors" and machine_choice == "paper":
    print(f"You win!. The machine chose {machine_choice}")
else:
    print(f"You lose! The machine chose {machine_choice}")

while True:
    pass
