username = input("Hi! Welcome to my program. What is your name? ")

# Keep asking yes/no until valid input
while True:
    yn = input(f"Hi {username}! Would you like to start the program? (Yes/No) ").lower().strip()
    
    if yn == 'yes':
        break  # Valid input, exit this loop and go to menu
    elif yn == 'no':
        print("Goodbye and Thank you.")
        exit()  # End program
    else:
        print("Please type Yes or No only.")



print("\n\t\tWELCOME TO NMPy PROGRAM!")

while True:
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
 
    choice = input("Select from the following options: ").lower()

    if choice == 'a':
        print("\n\t\tIntroduction to Programming\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()
        
            if dec == 'yes':
                print("\n============================================================================================\n\nINTRODUCTION TO PROGRAMMING\nContent:\n\nProgrammings is the process of giving instructions to a computer so it can perform tasks. \nThis particular programming language (Python) acts as a way for humans to communicate with machines.\n\nKey Points:\n\n\t1. Computer follows instructions step-by-step.\n\t2. Programming helps automate tasks, solve problems, and build apps.\n\t3. Python is popular because it's simple, readable andpowerful.\n\n============================================================================================\n")
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no'
    
        continue  # go back to the main menu

    elif choice == 'b':
        print("\n\t\tData Types & Variables\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()

            if dec == 'yes':
                print('\n============================================================================================\n\nDATA TYPES & VARIABLES\nContent:\n\nA variable stores a value so it can be used later.\nA data type tells the computer what kind of value is stored.\n\nCommon Python Data Types:\n\n1. int - whole numbers (e.g., 5, 20)\n2. float - decimal numbers (e.g., 3.14)\n3. str - text or characters (e.g., "Hello")\n4. bool - True or False values\n\nExample:\n\n\tage = 18\n\n\tpi = 3.14\n\n\tname = "Neil"\n\n\tis_student = True\n\n============================================================================================')
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no'

    elif choice == 'c':
        print("\n\t\tOperator & Expression\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()

            if dec == 'yes':
                print('\n============================================================================================\n\nOPERATORS & EXPRESSIONS\nContent:\n\nOperators allow you to perform actions on values.\n\nType of operators:\n\n\t1. Arithmetic: +, -, *, /, %, //, **\n\t2. Comparison: ==, !=, >, <, >=, <=\n\t3. Logical: and, or, not\n\nExample:\n\n\ta = 10\n\n\tb = 5\n\n\tresult = a + b\n\nExpressions combine values and operators to produce a result.\n\n============================================================================================')
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no'   

    elif choice == 'd':
        print("\n\t\tConditional Statements (if/else)\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()

            if dec == 'yes':
                print('\n============================================================================================\n\nCONDITIONAL STATEMENTS (IF/ELSE)\nContent:\n\nConditionals allow programs to make decisions.\n\nExample:\n\n\tage = 18\n\n\tif age >= 18:\n\t\tprint("You are an adult.)\n\telse:\n\t\tprint("You are a minor.)\n\nThe program chooses a path depending on whether conditions are true or false.\n\n============================================================================================')
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no'       

    elif choice == 'e':
        print("\n\t\tLoops (for/while)\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()

            if dec == 'yes':
                print('\n============================================================================================\n\nLOOPS (FOR/WHILE)\nContent:\n\nLoops repeat code multiple times.\n\nFor loop: repeats over a sequence.\n\n\tfor i in range(5):\n\t\tprint(i)\n\nWhile loop: repeats while a condition is true.\n\n\tcount = 1\n\twhile count <= 5:\n\t\tprint(count)\n\t\tcount += 1\n\nLoops help automate repetitive tasks.\n\n============================================================================================')
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no'     
    
    elif choice == 'f':
        print("\n\t\tFunctions\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()

            if dec == 'yes':
                print('\n============================================================================================\n\nFUNCTIONS\nContent:\n\nFunctions are reusable block of code that perform a specific task.\n\nExample:\n\n\tdef greet(name)\n\t\tprint("Hello,", name)\n\n\tgreet("Neil").\n\nFunction helps organize code and avoid repetition.\n\n============================================================================================')
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no' 

    elif choice == 'g':
        print("\n\t\tLists, Tuples, and Dictionaries\n")

        while True:
            dec = input("Proceed? (Yes/No): ").lower().strip()

            if dec == 'yes':
                print('\n============================================================================================\n\nLISTS, TUPLES, & DICTIONARIES\nContent:\n\nThese are basic Python data structures.\n\nList - changeable, ordered collection.\n\n\tfruits = ["apple", "banana", "mango"]\n\nTuple - ordered but unchangeable.\n\n\tpoint = (10,20)\n\nDictionary - stores key-value pairs.\n\n\tstudent = {"name": "Neil", "age: 18}\n\nEach structure has a unique purpose in organizing data.\n\n============================================================================================')
                break  # exit the dec loop and return to menu
            elif dec == 'no':
                break  # exit the dec loop and return to menu
            else:
                print("Please type Yes or No only.")
                       # Loop until user enters 'yes' or 'no' 
