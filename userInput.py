# name = input("Please enter your name: ")
# print ("Hello " + name)

# prompt = "If you want us to personalize your information, kindly give us your details"
# prompt += "\nwhat is you firstname and last name?: "

# #name = input(prompt)
# print("Hello, " + name + " welcome to the party!")

# age = input("how old are you? ")
# new_age = int(age)

# print("WOW! " + name + ' is ' + age + ' years old!')
# if new_age >= 23:
#     print('True')
# prompt = "Kindly enter your age: "

# age = input("Kindly enter your age: ")
# age = int(age)

# if age < 4:
#   price = 0
# elif age < 18:
#   price = 5
# else:
#    price = 10

# print("Your admission cost is $" + str(price) + ".")


# height = input("Please enter your height in inches: ")
# height = int(height)

# if height >= 30:
#   print("You are able to ride")

# else:
#   print("You are unable to ride, come back when you are abit taller!")

# number = input("enter a number, I will tell you whether it is an even or odd number: ")
# number = int(number)

# if number % 2 == 0:
#     print("\nThe number " + str(number) + " is even")
# else:
#     print("\nThe number is odd.")

# #WHILE LOOPS
# number = input("enter a number: ")
# number = int(number)

# current_number = number
# while current_number <= 10:
#     print(current_number)
#     current_number += 1

# rental_car = input("Please enter your rental car: ")
# print("Let me check if we still have the " + rental_car + " in stock!")

# dinner_group = input("How many people are in your dinner group?: ")
# dinner_group = int(dinner_group)

# if dinner_group >= 8:
#     print("Please wait for a bigger table.")
# else:
#     print("Your table is ready.")


# ####multiples of 10.
# num = input("Please enter a digit and i will tell you whether it is a multiple of 10 or not: ")
# num = int(num)

# if num % 10 == 0:
#     print(str(num) + " is a multiple of 10")
# else:
#     print(str(num) + " is not a multiple of 10.")

# prompt = "Enter something and i will repeat it to you."
# prompt += "\nEnter 'quit' to end this program."

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

# prompt = "Enter something and i will repeat it to you."
# prompt += "\nEnter 'quit' to end this program."

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "Enter a name of a city you have visited before."
# prompt += "\n(Enter 'quit' to end this program.) "
# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to visit {city.title()}")

# x = 1
# while x <= 5:
#     print(x)
#     x += 1

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)


###putting a dictionary into a list
# alienss = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     alienss.append(new_alien)

# for alien in alienss[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# for alien in alienss[3:7]:
#     if alien['color'] == 'green':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15

# ##first 5 aliens
# for alien in alienss[:10]:
#     print(alien)
# print(".......")

# ##total number of aliens
# print(f"Total number of aliens: {len(alienss)}")


##putting a list into a dictionary
# ##storing information about pizza being ordered
# pizza = {
#     'crust':'thick',
#     'toppings': ['mushroom', 'extra cheese']
# }
# print(f"You ordered a {pizza['crust']}-crust pizza " 
#       "with the following toppings: ")


# for topping in pizza['toppings']:
#     print(f"\t{topping}")

# ##removing from a dictionary
# pets = {'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'}
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')

# print(pets)

##writing to a dictionary
