import random
drinks = ["vodka", "tequila", "rum", "wine", "beer"]

try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = int(age)
except ValueError:
    print("Invalid age. please enter a number.")
else:
    if age < 0 or age > 140:
        print("You are not human, you cannot play.")
    elif age > 120
        print("You are too old to play this game.")
    elif age < 18:
        print("You are a minor. You can not play the drinking game")
    else:
        print("you are an adult. you can play the drinking game")
        print("Have some, ", random.choice(drinks), "and enjoy the game.")
