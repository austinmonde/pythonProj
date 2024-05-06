import random

def roll():
    min_value = 1
    max_value = 6
    roll_result = random.randint(min_value, max_value)

    return roll_result

value = roll()
print(value)

