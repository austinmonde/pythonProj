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
    
Print("Gooodbye!")