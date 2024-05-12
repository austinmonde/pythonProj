import random

options = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options: #checks whether user input is not in the list
        continue # the while loop will restart when the user does not enter anything in list

    random_number = random.randint(0, 2) # 0: Rock, 1: Paper, 2: Scissors
    computer_pick = options[random_number] #computer will pick from the index random numbers

    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins =+ 1
        
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins =+ 1
        
    elif user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins =+ 1
    else:
        print("You lost!")
        computer_wins =+ 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")

print("Gooodbye!")
input("Press Enter to exit...")