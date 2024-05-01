name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are in a dirt road, it has come to and you can go left or right, which way would you like to go?" ).lower()

if answer == "left":

elif answer == "right":

else:
    print('Not a valid option. You lose.')
