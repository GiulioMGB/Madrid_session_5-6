name = input("What is your name? ")
age = input("How old are you? ")
try:
    age = int(age)
    birth_year = 2023 - age
    print(name, ", you were born in ", birth_year, ".", sep="")

except:
    print("Invalid age. please enter a number.")