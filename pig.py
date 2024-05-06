import random

def roll():
    min_value = 1
    max_value = 6
    roll_result = random.randint(min_value, max_value)

    return roll_result

value = roll() #call the function and add it to variable value.
#print(value) #prints the result

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit(): #checks if the input provided by the user consists only of digits
        players = int(players)
        if 2 <= players <= 4: #checks if the number of players entered is between 2 and 4
            break
        else:
            print("Must be between 2 - 4 players")
    else:
        print("Invalid, try again.")
        
print(players)

    