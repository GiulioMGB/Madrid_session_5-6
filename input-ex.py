name = input("What is your name? ")
age = input("How old are you? ")

print("Hello, ", name, "!", sep="")

#convert a string into an integer
age = int(age)

birth_year = 2023 - age

print(name, ", you were born in ", birth_year, ".",  sep="")


