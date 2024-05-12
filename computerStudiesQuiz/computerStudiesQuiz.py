print("Welcome to my computer quiz")

playing = input('Do you want to play? ')
score = 0

if playing.lower() != "yes":
    print('See you next time.')
    quit()
print("okay let's play:) ")

question = input("What does RAM stand for? ").lower()
print(question)
if question == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does CPU stand for? ").lower()
print(question)
if question == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does GPU stand for? ").lower()
print(question)
if question == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does LAN stand for? ").lower()
print(question)
if question == "local area network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does URL stand for? ").lower()
print(question)
if question == "uniform resource locator":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does ROM stand for? ")
print(question)
if question == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does CLI stand for? ").lower()
print(question)
if question == "command line interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does VPN stand for? ").lower()
print(question)
if question == "virtual private network":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does GUI stand for? ").lower()
print(question)
if question == "graphical user interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

question = input("What does HTTP stand for? ").lower()
print(question)
if question == "hypertext transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "%.")

# Prompt the user to press Enter to exit
input("Press Enter to exit...")
