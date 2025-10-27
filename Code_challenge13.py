name = input("Hi, what's your name? ")

print("ODD NUMBER SELECTOR, press 0 to stop")

sum = 0
tuloy = True
odd = ""

while tuloy == True:
    number = eval(input("Enter a random number: "))

    if number % 2 == 1:
        print("This is an odd number")
        sum += number
        odd += str(number) + " "    
        continue

    elif number == 0:
        print("Loop terminated.")
        break

    else:
        if number % 2 == 0:
            print("This is an even number")
        else:
            print("Invalid number.")
            continue

print(f"Hi {name}, the sum of all the numbers you entered are: {sum}")
print(f"The odd numbers you entered are: {odd}")
