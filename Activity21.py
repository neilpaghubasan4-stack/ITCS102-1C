import random

print("Number Guessing Game")

random_number = random.randint(1,5)
tries = 0
tuloy = True

name = input("Hi, what's your name? ")

while tuloy == True:
    num = eval(input("Guess a number between 1 and 5: "))
    tries += 1
    if num == random_number:
        print("Winner!")
        break
    
    else:
        print("Try again.")
        continue

print(f"Congratulations {name}, you guessed the number {random_number} in {tries} tries!")
