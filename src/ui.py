import sys
"""
User interface for the calculator.
"""

def print_intro():
    print("***************************************************************\n")
    print("*** Welcome to SciCalc -- the simple scientific calculator! ***\n")
    print("***************************************************************\n")


def print_instructions():
    print("How to use SciCalc (in a nutshell):")
    print("Input a mathematical expression and hit enter to get the solution.")
    print("\nAllowed inputs:")
    print("* Numbers 0-9 (integer or floating point using the dot \".\" as the decimal separator)")
    print("* Other characters: brackets ( )")
    print("* Operators: plus +, minus -, muliplication *, division /, modulo mod or %, exponent ^ or **")
    print("* Functions: square root sqrt(), sine sin(), minimum min(), maximum max()")
    print("\nYou can also use the characters A-Z as variables and define them to have custom values")
    print("\nWhat would you like to do next?\n")


def print_commands():
    print("Commands:")
    print("1: Get a solution for an expression")
    print("2: Define a variable")
    print("3: List all defined variables")
    print("q: Quit SciCalc\n")


def main():
    print_intro()
    print_instructions()

    while True:
        print_commands()
        user_input = input("Please give a command:\n")
        print("\n*********************************")

        if user_input == "q":
            print("\n*** Quitting the program. Bye! ***")
            sys.exit()

        if user_input == "1":
            pass
        
        if user_input == "2":
            var_input = input("Which variable A-Z would you like to define")

        if user_input == "3":
            print("Defined variables:")
            print("You have no defined variables\n")

        print("*********************************")

