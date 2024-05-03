name = input("Type your name: ")
print("Welcome", name, "to this adventure")

weapons = ["knife", "gun", "axe"]

while True:
    answer = input("You are in a dirt road, it has come to an end and you can go left or right, which way would you like to go: ").lower()
    if answer == "left":
            answer = input("You come to a river, you can walk around it or swim across it, swim/walk: ").lower()
            if answer == "swim":
                print("You swam across and got eaten by an alligator. you lost the game.")
                quit()

            elif answer == "walk":
                print("You walked for many miles, ran out of water and lost the game ")
                quit()
            else:
                print('Not a valid option. You lose.')

    elif answer == "right":
        answer = input("You came across a bridge, it looks wobbly, do you want to cross it or headback (cross/back)?: ")
        if answer == "cross":
            answer = input("You have crosse on the wobbly bridge to the other side and came across a mountain (climb/go-round): ").lower()
            if answer == "climb":
                print("mountain was to high, ran out of water, you lose.")
                quit()
            elif answer == "go-round":
                answer = input("You went round and met a stranger, do you talk to them (yes/no)?: ").lower()
                if answer == "yes":
                    print("You talked and they gave you gold and water, YOU WIN! :)")

                elif answer == "no":
                    print("You ignored the stranger and they are you lose!")
                    quit()
                else:
                    print("Not a valid option you lose.")

            else:
                print('Not a valid option. You lose.')

        elif answer == "back":
            print("You went back, you lose")
            quit()

        else:
            print('Not a valid option. You lose.')  
    else:
        print('Not a valid option. You lose.')



    options = input("Press q to quit/ r to restart: ").lower()
    if options == "q":
        print("You quit, see you later!")
        quit()

    elif options == "r":
        continue
