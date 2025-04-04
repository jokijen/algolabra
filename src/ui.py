"""User interface for the calculator.
"""
from core.input_validator import InputValidator
from core.exceptions import InvalidExpressionException


# Intialise an empty dictionary for the user's variables
USER_VARS = {}
USER_VARS["A"] = "-4.5"
USER_VARS["B"] = "pi*3"
USER_VARS["C"] = "A+123"


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
    print("* Operators: plus '+', minus '-', multiplication '*', division '/', exponent '**'")
    print("* One argument functions: square root 'sqrt(x)', sine 'sin(x)', cosine 'cos(x)'")
    print("* Two argument functions: minimum 'min(x, y)', maximum 'max(x, y)'")
    print("* Other characters: brackets '(', ')', and comma ',' for max and min e.g. 'min(1, 9)'")
    print("\nYou can also use capital letters A-Z as variables and set values for them")


def print_commands():
    print("\nCommands:\n")
    print("1: Get a solution for an expression")
    print("2: Set a variable")
    print("3: List all defined variables")
    print("q: Quit SciCalc\n")


def print_expression_help():
    print_instructions()
    print("\nExpressions should be written with care in proper infix notation.")
    print("Minimum length: 1 character")
    print("Use a period '.' as a decimal separator.")
    print("Ensure brackets are correctly paired.")
    print("Be explicit with multiplication, e.g. use '3*A' instead of '3A")
    print("\nExample expressions:")
    print("'-2**2*-5.7'")
    print("'8.55 / max(sqrt(9), 4)+pi*3'")
    print("'3 * 4 + -5.67 / ( sin(9) + 2 ) * min(-5, -2.3)'")


def main(): # pylint: disable=too-many-statements
    validator = InputValidator(USER_VARS)
    # sy = ShuntingYard()
    # rpn_evaluator = RPNEvaluator

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

        if user_input == "1":
            while True:
                print("\nGive a mathematical expression to evaluate ('h' help, 'c' cancel):")
                expression_input = input(">>> ")
                print("")

                if expression_input == "c":
                    break

                if expression_input == "h":
                    print_expression_help()

                else:
                    try:
                        # TESTING: Valid:
                        # expression_input = "45.78- -56.7**sin(D)/sqrt(-9)+-max(3.5,-70)*pi*-6"
                        # Invalid:
                        # expression_input = "45.78- -56.7**sin(D)/sqrt(-9)+-max(3.5,-70)*pi*abc--6"

                        validated_expression = validator.validate_expression(expression_input)
                        # rpn_expression = sy.generate_RPN(validated_expression)
                        # result = rpn_evaluator(rpn_expression)

                        # print(result)
                        print(validated_expression)
                        # break

                    except InvalidExpressionException as e:
                        print(f"InvalidExpressionException: {e}")

        elif user_input == "2": # User defines a variable
            while True:
                print("\nWhich variable A-Z would you like to set? (e.g. 'A', or 'c' to cancel):")
                var_input = input(">>> ")

                if var_input == "c":
                    break

                # If the user gave a valid uppercase letter
                if validator.validate_var_character(var_input):

                    while True:
                        val_input = input(f"\nGive value for {var_input}: ")

                        try: # Set variable or give an error
                            USER_VARS.update({var_input: val_input})
                            validator.update_user_vars(USER_VARS)
                            print(f"\nVariable {var_input} = {val_input} set!")
                            break
                        except ValueError:
                            print("\nInvalid input.")
                    break

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
