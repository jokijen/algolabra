import sys
from core.input_validator import InputValidator
from core.exceptions import InvalidExpressionException
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


def print_separator():
    print("\n" + "*" * 50)


def print_instructions():
    print("How to use SciCalc (in a nutshell):")
    print("Input a mathematical expression and hit enter to get the solution.")
    print("\nAllowed inputs:")
    print("* Numbers 0-9 (integer or floating point using the dot '.' as the decimal separator)")
    print("* Constants: 'pi'")
    print("* Operators: plus '+', minus '-', muliplication '*', division '/', exponent '**'")
    print("* Functions: square root 'sqrt(x)', sine 'sin(x)', cosine 'cos(x)', minimum 'min(x, y)', maximum 'max(x, y)'")
    print("* Other characters: brackets '(', ')', and comma ',' for max and min e.g. 'min(1, 9)'")
    print("\nYou can also use capital letters as variables and define them to have custom values")


def print_commands():
    print("Commands:")
    print("1: Get a solution for an expression")
    print("2: Define a variable")
    print("3: List all defined variables")
    print("q: Quit SciCalc\n")


def print_expression_help():
    print_instructions()
    print("\nExpressions should be written with care in proper infix notation.")
    print("Minimum length: 3 characters")
    print("Use a period '.' as a decimal separator, and ensure brackets are correctly paired.")
    print("Be explicit with multiplication, e.g. use '3*A' instead of '3A")
    print("\nExample expressions:")
    print("'-2**2*-5.7'")
    print("'8.55 / max(sqrt(9), 4)+pi*3'")
    print("'3 * 4 + -5.67 / ( sin(9) + 2 ) * min(-5, -2.3)'")


def main():
    print_intro()
    print_instructions()
    print("\nWhat would you like to do next?\n")

    while True:
        print_commands()
        user_input = input("Please give a command:\n>>> ")
        print_separator()

        if user_input == "q":
            print("\n*** Quitting the program. Bye! ***\n")
            break

        elif user_input == "1":
            while True:
                expression_input = input("\nGive a mathematical expression to evaluate ('h' instructions, 'q' cancel):\n>>> ")
                print("")

                if expression_input == "q": 
                    break

                elif expression_input == "h":
                    print_expression_help()

                else:
                    try:
                        validator = InputValidator(USER_VARS)
                        # sy = ShuntingYard()
                        # rpn_evaluator = RPNEvaluator

                        # TESTING: Valid:
                        # expression_input = "45.78- -56.7**sin(D)/sqrt(-9)+-max(3.5,-70)*pi*-6" #For testing
                        # Invalid:
                        # expression_input = "45.78- -56.7**sin(D)/sqrt(-9)+-max(3.5,-70)*pi*abc--6" #For testing

                        validated_expression = validator.validate_expression(expression_input)
                        # rpn_expression = sy.generate_RPN(validated_expression)
                        # result = rpn_evaluator(rpn_expression)

                        # print(result)
                        print(validated_expression)

                    except InvalidExpressionException as e:
                        print(f"InvalidExpressionException: {e}")
        
        elif user_input == "2": # User defines a variable
            while True:
                var_input = input("\nWhich variable A-Z would you like to define? (e.g. 'A', or 'q' to cancel):\n>>> ")

                if var_input == "q":
                    break

                # Ensure that user gave an uppercase letter
                if InputValidator.validate_var_character(var_input):

                    while True:
                        val_input = input(f"\nGive value for {var_input}: ")
                        
                        try: # Set variable if it is an int or float number, else give error
                            valid_value = InputValidator.validate_var_value(val_input)
                            USER_VARS.update({var_input: valid_value})
                            print("\nVariable set!")
                            break
                        except ValueError:
                            print("\nInvalid input. Please enter a number (e.g. '1.45')")
                    break
                else:
                    print("\nThat is not a valid variable. Please try again.")


        elif user_input == "3":
            print("\nDefined variables:\n")
            if not USER_VARS: 
                print("You have no defined variables\n")
                continue
            for key, value in USER_VARS.items():
                print(f"{key} = {value}")
        
        else:
            print("\nNice try! That is not a valid command. Try again.")

        print_separator()
