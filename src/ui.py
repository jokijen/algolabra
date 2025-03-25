import sys
from core.input_validator import validate_var_value
"""
User interface for the calculator.
"""

# Intialise an empty dictionary for the user's variables
USER_VARS = {}
USER_VARS["A"] = -4.5

def print_intro():
    print("***************************************************************\n")
    print("*** Welcome to SciCalc -- the simple scientific calculator! ***\n")
    print("***************************************************************\n")


def print_instructions():
    print("How to use SciCalc (in a nutshell):")
    print("Input a mathematical expression and hit enter to get the solution.")
    print("\nAllowed inputs:")
    print("* Numbers 0-9 (integer or floating point using the dot \".\" as the decimal separator)")
    print("* Operators: plus +, minus -, muliplication *, division /, modulo mod or %, exponent ^ or **")
    print("* Functions: square root sqrt(), sine sin(), minimum min(), maximum max()")
    print("* Other characters: brackets ( ), and comma for max and min e.g. min(1, 9)")
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
        print("\n**********************************\n")

        if user_input == "q":
            print("*** Quitting the program. Bye! ***\n")
            break

        elif user_input == "1":
            pass
        
        elif user_input == "2": # User defines a variable
            while True:
                var_input = input("Which variable A-Z would you like to define? (e.g. 'A'): ")

                if var_input == "q":
                    break

                # Ensure that user gave an uppercase letter
                if var_input.isupper() and len(var_input) == 1:

                    while True:
                        val_input = input(f"\nGive value for {var_input}: ")
                        
                        try: # Set variable if it is an int or float number, else give error
                            valid_value = validate_var_value(val_input)
                            USER_VARS.update({var_input: valid_value})
                            print("\nVariable set!")
                            break
                        except ValueError:
                            print("\nInvalid input. Please enter a number (e.g. '1.45')")
                    break
                else:
                    print("\nThat is not a valid variable. Please try again.\n")


        elif user_input == "3":
            print("Defined variables:\n")
            if not USER_VARS: 
                print("You have no defined variables\n")
                continue
            for key, value in USER_VARS.items():
                print(f"{key} = {value}")
        
        else:
            print("Nice try! That is not a valid command. Try again. \n")

        print("\n**********************************\n")

