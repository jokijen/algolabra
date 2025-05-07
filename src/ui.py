"""User interface for the calculator.
"""
import string
from core.exceptions import InvalidExpressionException
from core.input_validator import InputValidator
from core.shunting_yard import ShuntingYard
from core.rpn_evaluator import RPNEvaluator
from utils import printer


# Intialise an empty dictionary for the user's variables
USER_VARS = {}

# Formatting for the CLI
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"


def get_user_command():
    """Queries the user for a command that determines the action taken by the application.
    
    Returns: The user's command (string)
    """
    printer.print_command_options()
    user_command = input("Please give a command:\n>>> ")
    printer.print_separator()

    return user_command

def evaluate_expression(validator: InputValidator, sy: ShuntingYard, rpn_evaluator: RPNEvaluator):  # pylint: disable=too-many-statements
    """Queries the user for an expression to evaluate and possibly set as the value of a variable.
    Validates, tokenises, converts to RPN/postfix, and evaluates the expression.
    Sets the variable if necessary.

    Args:
        validator -- InputValidator object whose method validate_expression() is called to validate the
            user's string type expression and convert it into valid tokens
        sy -- ShuntingYard object whose method convert_to_rpn() is called to convert the tokenised infix
            expression to RPN/postfix form (type: Queue)
        rpn_evaluator -- RPNEvaluator object whose method evaluate_rpn_expression() is called to evaluate
            the postfix expression Queue

    Returns: Nothing if successful. The value of the expression is printed as output
    """
    while True:
        print(f"\n{BOLD}Give a mathematical expression to evaluate ('h' help, 'c' cancel):{RESET}")
        expression_input = input(">>> ")

        if expression_input == "c":
            return

        if expression_input == "h":
            printer.print_expression_help()

        else:
            try:
                validated_expression = validator.validate_expression(expression_input)
                # Variable the user wants to set. Capital ASCII e.g. "A"
                var_to_set = validated_expression[1]

                if var_to_set:
                    print("\nVariable to set:")
                    print(var_to_set)

                print("\nValidated tokens:")
                print(validated_expression[0])

            except InvalidExpressionException as e:
                print(f"\n{UNDERLINE}Validation error:{RESET} {e}")
                continue

            try:
                rpn_expression = sy.convert_to_rpn(validated_expression[0])
                print("\nReverse Polish Notation (RPN):")
                print(rpn_expression)

            except InvalidExpressionException as e:
                print(f"\n{UNDERLINE}Error when converting to RPN:{RESET} {e}")
                continue

            try:
                end_result = rpn_evaluator.evaluate_rpn_expression(rpn_expression)
                print("\nFinal result:")
                print(end_result)

            except InvalidExpressionException as e:
                print(f"\n{UNDERLINE}Error when evaluating the RPN expression:{RESET} {e}")
                continue

            if var_to_set:
                set_variable(var_to_set, end_result, validator)

            return

def set_variable(var_to_set: str, var_value: int | float, validator: InputValidator):
    """Sets the value for the variable specified by the user. If the variable is already in use, allows
    the user to overwrite the old value, continue without updating any variable, or choose a new variable
    to update with the value. In the last case, the same options are presented to the user if the new
    variable already has a value as well. 

    Args:
        var_to_set -- Variable the user wishes to set, capital ASCII A-Z
        var_value -- Integer or floating point value for the variable
        validator -- InputValidator object whose method update_user_variable() is called to update the
            user variables of the object as well

    Returns: Nothing if successful. The action taken is printed as output
    """
    while True:
        if var_to_set in USER_VARS:
            print(f"\nThe variable {var_to_set} already has a value. Do you want to "
                  "overwrite value? \n[y (yes) / n (no) / A-Z (to select new variable)]")
            choice = input(">>> ")

            if choice in string.ascii_uppercase and len(choice) == 1:
                var_to_set = choice
                continue

            if choice == "y":
                break

            if choice == "n":
                print("\nVariable not updated")
                return

            print("\nInvalid command. Please try again.")
            continue
        break

    USER_VARS.update({var_to_set: var_value})
    validator.update_user_variable(var_to_set, var_value)
    print(f"\nVariable {var_to_set} = {var_value} set!")
    return

def main():
    """The main function for the application that queries the user for commands that determine which action
    to take. Exiting the while loop terminates the application. 

    Returns: Nothing if successful. Instructions are printed as output
    """
    validator = InputValidator(USER_VARS)
    sy = ShuntingYard()
    rpn_evaluator = RPNEvaluator()

    printer.print_intro()
    printer.print_instructions()
    print("\nWhat would you like to do next?")

    while True:
        user_command = get_user_command()

        if user_command == "q":
            printer.print_outro()
            break

        # Solve a mathematical expression
        if user_command == "1":
            evaluate_expression(validator, sy, rpn_evaluator)

        # Print all defined variables and their values in alphabetical order
        elif user_command == "2":
            printer.print_variables(USER_VARS)

        else:
            print("\nNice try! That is not a valid command. Try again.")

        printer.print_separator()
