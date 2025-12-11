# NMPy Program (function-based, beginner friendly)
# Author: Neil (NMP)
# Purpose: Teaching basic programming concepts with a menu and functions

def get_yes_no(prompt):
    """
    Ask the user a Yes/No question until they enter a valid answer.
    Returns 'yes' or 'no'.
    """
    while True:
        answer = input(prompt).lower().strip()
        if answer == 'yes' or answer == 'y':
            return 'yes'
        elif answer == 'no' or answer == 'n':
            return 'no'
        else:
            print("Please type Yes or No only (yes/no).")

def pause():
    """Pause so the user can read content before returning to the menu."""
    input("\nPress Enter to return to the main menu...")

def introduction():
    print("\n\t\tIntroduction to Programming\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

INTRODUCTION TO PROGRAMMING
Content:

Programming is the process of giving instructions to a computer so it can perform tasks.
This particular programming language (Python) acts as a way for humans to communicate with machines.

Key Points:

    1. Computers follow instructions step-by-step.
    2. Programming helps automate tasks, solve problems, and build apps.
    3. Python is popular because it's simple, readable, and powerful.

============================================================================================
""")
        pause()

def data_types():
    print("\n\t\tData Types & Variables\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

DATA TYPES & VARIABLES
Content:

A variable stores a value so it can be used later.
A data type tells the computer what kind of value is stored.

Common Python Data Types:

1. int   - whole numbers (e.g., 5, 20)
2. float - decimal numbers (e.g., 3.14)
3. str   - text or characters (e.g., "Hello")
4. bool  - True or False values

Example:

    age = 18
    pi = 3.14
    name = "Neil"
    is_student = True

============================================================================================
""")
        pause()

def operators_expressions():
    print("\n\t\tOperators & Expressions\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

OPERATORS & EXPRESSIONS
Content:

Operators allow you to perform actions on values.

Types of operators:

    1. Arithmetic: +, -, *, /, %, //, **
    2. Comparison: ==, !=, >, <, >=, <=
    3. Logical: and, or, not

Example:

    a = 10
    b = 5
    result = a + b  # 15

Expressions combine values and operators to produce a result.

============================================================================================
""")
        pause()

def conditionals_section():
    print("\n\t\tConditional Statements (if/else)\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

CONDITIONAL STATEMENTS (IF/ELSE)
Content:

Conditionals allow programs to make decisions.

Example:

    age = 18

    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")

The program chooses a path depending on whether conditions are true or false.

============================================================================================
""")
        pause()

def loops_section():
    print("\n\t\tLoops (for/while)\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

LOOPS (FOR/WHILE)
Content:

Loops repeat code multiple times.

For loop: repeats over a sequence.

    for i in range(5):
        print(i)

While loop: repeats while a condition is true.

    count = 1
    while count <= 5:
        print(count)
        count += 1

Loops help automate repetitive tasks.

============================================================================================
""")
        pause()

def functions_section():
    print("\n\t\tFunctions\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

FUNCTIONS
Content:

Functions are reusable blocks of code that perform a specific task.

Example:

    def greet(name):
        print("Hello,", name)

    greet("Neil")

Functions help organize code and avoid repetition. They can also accept parameters
and return values.

Simple function example with return:

    def add(a, b):
        return a + b

============================================================================================
""")
        # Simple interactive demo of a function
        follow = get_yes_no("Would you like to try a small function demo? (Yes/No): ")
        if follow == 'yes':
            try:
                x = int(input("Enter first number (integer): "))
                y = int(input("Enter second number (integer): "))
                def add(a, b):
                    return a + b
                print(f"The sum of {x} and {y} is {add(x, y)}.")
            except ValueError:
                print("That wasn't an integer. Demo skipped.")
        pause()

def structures_section():
    print("\n\t\tLists, Tuples, and Dictionaries\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

LISTS, TUPLES, & DICTIONARIES
Content:

These are basic Python data structures.

List - changeable, ordered collection.

    fruits = ["apple", "banana", "mango"]

Tuple - ordered but unchangeable.

    point = (10, 20)

Dictionary - stores key-value pairs.

    student = {"name": "Neil", "age": 18}

Each structure has a unique purpose in organizing data.

============================================================================================
""")
        # Small interactive demo
        follow = get_yes_no("Would you like to try a short demo? (Yes/No): ")
        if follow == 'yes':
            fruits = []
            print("Let's add 3 fruits to a list.")
            for i in range(3):
                f = input(f"Enter fruit #{i+1}: ")
                fruits.append(f)
            print("Your fruits list is:", fruits)
            tup = tuple(fruits)
            print("As a tuple (immutable):", tup)
            student = {"name": input("Enter a name for a sample student: "), "age": 18}
            print("Sample dictionary:", student)
        pause()

def io_section():
    print("\n\t\tBasic Input/Output\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        print("""
============================================================================================

BASIC INPUT / OUTPUT
Content:

Input allows users to type something.
Output displays information on the screen.

Example:

    name = input("Enter your name: ")
    print("Hello,", name)

Python uses input() to receive data and print() to show data.

============================================================================================
""")
        # Demo: ask name and show formatted output
        follow = get_yes_no("Would you like to try an input/output demo? (Yes/No): ")
        if follow == 'yes':
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            print("Simple output examples:")
            print("Hello,", name)
            print("You are " + age + " years old.")
            print(f"Using f-strings: {name} is {age} years old.")
        pause()

def mini_quiz():
    print("\n\t\tMini Coding Quiz\n")
    dec = get_yes_no("Proceed? (Yes/No): ")
    if dec == 'yes':
        score = 0
        print("\n============================================================================================")
        print("MINI QUIZ — Answer in lowercase only!")
        print("============================================================================================\n")
        q1 = input("1. What keyword is used to define a function in Python? ")
        if q1.strip().lower() == "def":
            score += 1
        q2 = input("2. Which data type holds text? (int, float, str) ")
        if q2.strip().lower() == "str":
            score += 1
        q3 = input("3. What loop repeats a block while a condition is true? ")
        if q3.strip().lower() == "while":
            score += 1
        q4 = input("4. Which operator checks equality? (==, =, !=) ")
        if q4.strip().lower() == "==":
            score += 1
        q5 = input("5. Which data structure uses key-value pairs? (list, tuple, dict) ")
        if q5.strip().lower() in ("dict", "dictionary"):
            score += 1
        print(f"\nYour Score: {score}/5")
        if score == 5:
            print("Excellent! You know the basics well.")
        elif score >= 3:
            print("Good job! A little more practice and you'll be great.")
        else:
            print("Keep studying — practice makes perfect.")
        print("============================================================================================\n")
        pause()

def goodbye():
    print("\nThank you for using NMPy Program. Goodbye!")
    # Use exit() to end the program
    exit()

def show_menu():
    print("\n\t\tWELCOME TO NMPy PROGRAM!\n")
    print("\n============================================================================================\n")
    print("\t\tNMPy PROGRAM CONTENTS:\n")
    print("\tA - Introduction to Programming")
    print("\tB - Data Types & Variables")
    print("\tC - Operators & Expressions")
    print("\tD - Conditional Statements (if/else)")
    print("\tE - Loops (for/while)")
    print("\tF - Functions")
    print("\tG - Lists, Tuples, and Dictionaries")
    print("\tH - Basic Input/Output")
    print("\tI - Mini Coding Quiz")
    print("\tJ - Exit Program\n")

def main():
    # greet and ask name
    username = input("Hi! Welcome to my program. What is your name? ")

    # ask to start program (validated)
    yn = get_yes_no(f"Hi {username}! Would you like to start the program? (Yes/No): ")
    if yn == 'no':
        print("Goodbye and Thank you.")
        return

    # Main menu loop
    while True:
        show_menu()
        choice = input("Select from the following options: ").lower().strip()
        if choice == 'a':
            introduction()
        elif choice == 'b':
            data_types()
        elif choice == 'c':
            operators_expressions()
        elif choice == 'd':
            conditionals_section()
        elif choice == 'e':
            loops_section()
        elif choice == 'f':
            functions_section()
        elif choice == 'g':
            structures_section()
        elif choice == 'h':
            io_section()
        elif choice == 'i':
            mini_quiz()
        elif choice == 'j':
            goodbye()
        else:
            print("Invalid choice. Please type a letter from A to J.")

# Run the program
if __name__ == "__main__":
    main()
