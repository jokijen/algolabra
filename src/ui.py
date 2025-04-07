"""User interface for the calculator.
"""
from core.input_validator import InputValidator
from core.exceptions import InvalidExpressionException
from core.shunting_yard import ShuntingYard


# Intialise an empty dictionary for the user's variables
USER_VARS = {}
USER_VARS["A"] = "-4.5"
USER_VARS["B"] = "pi*3"
USER_VARS["C"] = "A+123"

USER_VARS["X"] = "Y"
USER_VARS["Y"] = "Z"
USER_VARS["Z"] = "X"


def print_intro():
    print("***************************************************************\n")
    print("*** Welcome to SciCalc -- the simple scientific calculator! ***\n")
    print("***************************************************************\n")
    print("SciCalc (in a nutshell):")
    print("Give a mathematical expression and get the solution.")


def print_separator():
    print("\n" + "*" * 50)


def print_instructions():
    print("\nAllowed inputs:\n")
    print("* Numbers 0-9 (integer or floating point using the period '.' as the decimal separator)")
    print("* Constants: 'pi'")
    print("* Operators: plus '+', minus '-', multiplication '*', division '/', exponent '**'")
    print("* One argument functions: square root 'sqrt(x)', sine 'sin(x)', cosine 'cos(x)'")
    print("* Two argument functions: minimum 'min(x, y)', maximum 'max(x, y)'")
    print("* Other characters: brackets '(', ')', and comma ',' for max and min e.g. 'min(1, 9)'")
    print("\nYou can also use capital letters A-Z as variables and set values for them.")
    print("The allowed inputs for variable values are the same as above, but the validity " \
    "will only be checked when the variable is used in an expression.")
    print("Nested variables are allowed, but make sure they don't form an infinite cycle.")


def print_commands():
    print("\nCommands:\n")
    print("1: Get a solution for an expression")
    print("2: Set a variable")
    print("3: List all defined variables")
    print("q: Quit SciCalc\n")


def print_expression_help():
    print_instructions()
    print("\nExpressions should be written with care in proper infix notation.")
    print("Spaces don't matter. Use them if you like them.")
    print("Use a period '.' as a decimal separator.")
    print("Ensure brackets are correctly paired.")
    print("Be explicit with negative numbers and enclose them in brackets, e.g. '(-3)'. not '-3")
    print("Be explicit with multiplication, e.g. '3*A', not '3A")
    print("\nExample expressions:")
    print("'(-2)**2*(-5.7)'")
    print("'8.55 / max(sqrt(9), 4) + pi*3'")
    print("'3 * 4 + (-5.67) / (sin(9) + 2) * min((-5), (-2.3))'")


def main(): # pylint: disable=too-many-statements
    validator = InputValidator(USER_VARS)
    # sy = ShuntingYard()
    # rpn_evaluator = RPNEvaluator

    print_intro()
    print_instructions()
    print("\nWhat would you like to do next?")

    while True:
        print_commands()
        user_input = input("Please give a command:\n>>> ")
        print_separator()

        if user_input == "q":
            print("\n*** Quitting the program. Bye! ***\n")
            break

        # Solve a mathematical expression
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
                    print("Original expression:", expression_input)
                    try:
                        # TESTING: Valid:
                        # expression_input = "45.78- -56.7**sin(D)/sqrt(-9)+-max(3.5,-70)*pi*-6"
                        # Invalid:
                        # expression_input = "45.78- -56.7**sin(D)/sqrt(-9)+-max(3.5,-70)*pi*abc--6"

                        validated_expression = validator.validate_expression(expression_input)
                        print("Tokenised expression:", validated_expression)

                        # rpn_expression = sy.convert_to_rpn(validated_expression)
                        # result = rpn_evaluator(rpn_expression)
                        
                        # print("Reverse Polish Notation (RPN):", rpn_expression)
                        break

                    except InvalidExpressionException as e:
                        print(f"InvalidExpressionException: {e}")

        # Set a variable
        elif user_input == "2":
            while True:
                print("\nWhich variable A-Z would you like to set? (e.g. 'A', or 'c' to cancel):")
                var_input = input(">>> ")

                if var_input == "c":
                    break

                # The user gives a valid uppercase letter
                if validator.validate_var_character(var_input):
                    if var_input in USER_VARS:
                        print("\nThe variable already has a value. ('c' cancel or anything else to continue)")
                        command = input(">>> ")

                        if command == "c":
                            continue

                    while True:
                        val_input = input(f"\nGive value for {var_input}: ")

                        try:
                            USER_VARS.update({var_input: val_input})
                            validator.update_user_vars(USER_VARS)
                            print(f"\nVariable {var_input} = {val_input} set!")
                            break
                        except ValueError:
                            print("\nInvalid input.")
                    break

                print("\nThat is not a valid variable. Please try again.")

        # Print all defined variables and their values
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
