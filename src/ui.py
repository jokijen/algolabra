"""User interface for the calculator.
"""
import string
from core.exceptions import InvalidExpressionException
from core.input_validator import InputValidator
from core.shunting_yard import ShuntingYard
from core.rpn_evaluator import RPNEvaluator

# Intialise an empty dictionary for the user's variables
USER_VARS = {}
USER_VARS["A"] = -4.5

def print_intro():
    print("***************************************************************\n")
    print("*** Welcome to SciCalc -- the simple scientific calculator! ***\n")
    print("***************************************************************\n")
    print("SciCalc (in a nutshell):")
    print("Give a mathematical expression and get the solution.")


def print_separator():
    print("\n" + "*" * 70)


def print_instructions():
    print("\nAllowed inputs:\n")
    print("* Numbers 0-9 (integer or floating point using the period '.' as the decimal separator)")
    print("* Constants: 'pi'")
    print("* Operators: plus '+', minus '-', multiplication '*', division '/', exponentiation '**'")
    print("* One argument functions: square root 'sqrt(x)', sine 'sin(x)', cosine 'cos(x)' "
        "(note!: When using 'sin' and 'cos', 'x' will be converted to radians first, so use degrees)")
    print("* Two argument functions: minimum 'min(x, y)', maximum 'max(x, y)'")
    print("* Other characters: brackets '(', ')', and comma ',' for max and min e.g. 'min(1, 9)'")
    print("\nYou can also use capital letters A-Z as variables and set values for them.")
    print("The allowed inputs for variable values are the same as above, but the validity "
          "will only be checked when the variable is used in an expression.")
    print("Nested variables are allowed, but make sure they don't form an infinite cycle.")


def print_commands():
    print("\nCommands:\n")
    print("1: Get a solution for an expression or set a variable")
    print("2: List all defined variables")
    print("q: Quit SciCalc\n")


def print_expression_help():
    print_instructions()
    print("\nExpressions should be written with care in proper infix notation.")
    print("Spaces are not necessary, but can  be used between operators, operands and functions.")
    print("Use a period '.' as a decimal separator, not a comma ','.")
    print("Ensure brackets are correctly paired.")
    print("Be explicit with negative numbers and enclose them in brackets, e.g. '(-3)'. not '-3")
    print("Be explicit with multiplication, e.g. '3*A', not '3A")
    print("\nExample expressions:")
    print("Valid: '(-2)**2*(-5.7)'")
    print("Valid: '8.55 / max(sqrt(9), 4) + pi*3'")
    print("Valid: '3 * 4 + (-5.67) / (sin(9) + 2) * min((-5), (-2.3))'")
    print("\nNot valid: '(- 2)**a*(-5.7)' (space after unary negative; invalid character)")
    print("              ^    ^")
    print("Not valid: '8,5/(max(sqrt(9), -4)+pi' (comma instead of period; "
          "negative number not in brackets)")
    print("             ^                ^")
    print("Not valid: '3 / 3A + 2) / 0' (inexplicit multiplication; division with zero)")
    print("                 ^        ^")


def main():  # pylint: disable=too-many-statements
    validator = InputValidator(USER_VARS)
    sy = ShuntingYard()
    rpn_evaluator = RPNEvaluator()

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
                    print("Original expression:")
                    print(expression_input)

                    try:
                        validated_expression = validator.validate_expression(expression_input)
                        # Variable the user wants to set e.g. "A"
                        var_to_set = validated_expression[1]
                        print("\nValidated tokens:")
                        print(validated_expression[0])

                    except InvalidExpressionException as e:
                        print(f"Validation error: {e}")
                        continue

                    try:
                        rpn_expression = sy.convert_to_rpn(validated_expression[0])
                        print("\nReverse Polish Notation (RPN):")
                        print(rpn_expression)

                    except InvalidExpressionException as e:
                        print(f"Error when converting to RPN: {e}")
                        continue

                    try:
                        end_result = rpn_evaluator.evaluate_rpn_expression(rpn_expression)
                        print("\nFinal result:")
                        print(end_result)

                    except InvalidExpressionException as e:
                        print(f"Error when evaluating the RPN expression: {e}")
                        continue

                    if var_to_set:
                        while True:
                            if var_to_set in USER_VARS:
                                print(f"\nThe variable {var_to_set} already has a value. Do you want to "
                                      "overwrite value?")
                                print("[y (yes) / n (no) / A-Z (to select new variable)]")
                                command = input(">>> ")

                                if command in string.ascii_uppercase:
                                    var_to_set = command
                                    continue

                                if command == "y":
                                    USER_VARS.update({var_to_set: end_result})
                                    validator.update_user_vars(var_to_set, end_result)
                                    print(f"\nVariable {var_to_set} = {end_result} set!")
                                    break

                                if command == "n":
                                    print("\nVariable not updated")
                                    break

                                print("Invalid command. Please try again.")

                            USER_VARS.update({var_to_set: end_result})
                            validator.update_user_vars(var_to_set, end_result)
                            print(f"\nVariable {var_to_set} = {end_result} set!")
                            break

                    print_separator()


        # Print all defined variables and their values in alphabetical order
        elif user_input == "2":
            print("\nDefined variables:\n")
            if not USER_VARS:
                print("You have no defined variables\n")
                continue
            for key in sorted(USER_VARS.keys()):
                print(f"{key} = {USER_VARS[key]}")

        else:
            print("\nNice try! That is not a valid command. Try again.")

        print_separator()
