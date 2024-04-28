import random

top_of_number = input("Type in a number: ") #user input

if top_of_number.isdigit(): #checks whether entered number is a digit
    top_of_number = int(top_of_number) #converts number from string to an integer

    if top_of_number <= 0: #number entered by user should not be less than 0
        print("Please enter a number larger than 0 next time.")
        quit() #if number is less or equal to 0 quit program

else:
    print("Please enter a number next time")
    quit()

##if there is no error code will proceed to the next lines of code:)

guesses = 0 #this will keep count of the number of guesses the user did.

random_number = random.randint(0, top_of_number) #generate upto number entered by user

while True: #the code will keep running unless it is false
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit(): #checks whether entered number is a digit
        user_guess = int(user_guess) #converts number from string to an integer

    else:
        print("Please enter a number next time")
        continue #this will continue restart the while loop till user types a number.
    
    if user_guess == random_number: 
        print("You got it correct!") # this line will not be printed unless user gets the guess correct.
        break

    ##elif will help by checking another condition if the initial condition is not true.
    elif user_guess > random_number: #This will help the user narrow down their guess.
            print("You we're above the number!")
    else:
        print("You were below the number!")

print("You got it in ", guesses, "guesses.")
