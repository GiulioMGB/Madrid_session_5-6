name = input("What is your name? ")
age = input("How old are you? ")
try:
    age = int(age)
    birth_year = 2023 - age
    print(name, ", you were born in ", birth_year, ".", sep="")
    number = input("Give me a number to divide the age ")
    number = int(number)
    print(age/number)
except ValueError:
    print("Invalid age. please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

except:
    print("Some other error that i did not forsee")

else:
    print("No exceptions were raised")

finally:
    print("Thanks for playing")
