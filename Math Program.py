import random

def Addition():

    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    result = first_number + second_number

    user_input = int(input("What is " + str(first_number) + "+" + str(second_number) + "="))
    if user_input == result:
        print("Well done!  That's correct.  The answer is", result)
    else:
        print("I'm sorry. "  "That's incorrect.  The answer is", result)

    try_again = input("Would you like to try again? (y) or (n)")

    invalid_response = True

    while invalid_response:
        if try_again == "y":
            Addition()
        elif try_again == "n":
            operations_menu()
        else:
            print("That's not a valid response.")
            try_again = input("Would you like to try again? (y) or (n)")

def Subtraction():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    if second_number > first_number:
        first_number = second_number + random.randint(1, 5)
    result = first_number - second_number

    user_input = int(input("What is " + str(first_number) + "-" + str(second_number) + "="))
    if user_input == result:
        print("Well done!  That's correct.  The answer is", result)
    else:
        print("I'm sorry. "  "That's incorrect.  The answer is", result)

    try_again = input("Would you like to try again? (y) or (n)")

    invalid_response = 0

    while invalid_response < 3:
        if try_again == "y":
            Subtraction()
        elif try_again == "n":
            operations_menu()
        else:
            print("That's not a valid response.")
            try_again = input("Would you like to try again? (y) or (n)")
            invalid_response = invalid_response + 1

def Multiplication():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    result = first_number * second_number

    user_input = int(input("What is " + str(first_number) + "*" + str(second_number) + "="))

    if user_input == result:
        print("Well done!  That's correct.  The answer is", result)
    else:
        print("I'm sorry. "  "That's incorrect.  The answer is", result)

    try_again = input("Would you like to try again? (y) or (n)")

    invalid_response = 0

    while invalid_response < 3:
        if try_again == "y":
            Multiplication()
        elif try_again == "n":
            operations_menu()
        else:
            print("That's not a valid response.")
            try_again = input("Would you like to try again? (y) or (n)")
            invalid_response = invalid_response + 1

def Division():
    first_number = random.randrange(2, 10, 2)
    second_number = random.randrange(2, 10, 2)
    if second_number > first_number:
        first_number = second_number + random.randrange(2, 10, 2)
    result = first_number / second_number

    user_input = float(input("What is " + str(first_number) + "/" + str(second_number) + "="))

    if user_input == result:
        print("Well done!  That's correct.  The answer is", result)
    else:
        print("I'm sorry. "  "That's incorrect.  The answer is", result)

    try_again = input("Would you like to try again? (y) or (n)")

    invalid_response = 0

    while invalid_response < 3:
        if try_again == "y":
            Division()
        elif try_again == "n":
            operations_menu()
        else:
            print("That's not a valid response.")
            try_again = input("Would you like to try again? (y) or (n)")
            invalid_response = invalid_response + 1

user = input("Welcome to fun with math.  What is your name? ")
print("Hello", user + "." +  " Let's do some math.")

def operations_menu():
    operations_list = ["Addition", "Subtraction", "Multiplication", "Division", "Exit"]

    print("\n1. ", operations_list[0])
    print("2. ", operations_list[1])
    print("3. ", operations_list[2])
    print("4. ", operations_list[3])
    print("5. ", operations_list[4])

    selection = input("Please make a selection.")

    if selection == "1":
        print("Ok.  Can you answer this addition question? ")
        Addition()
    elif selection == "2":
        print("Ok.  Can you answer this subtraction question? ")
        Subtraction()
    elif selection == "3":
        print("Ok.  Can you answer this multiplication question? ")
        Multiplication()
    elif selection == "4":
        print("Ok.  Can you answer this division question? ")
        Division()
    elif selection == "5":
        print("Ok. Bye! ")
    else:
        print("That's not a valid response.")
        try_again = input("Please select a number between 1 - 5.")

operations_menu()





























