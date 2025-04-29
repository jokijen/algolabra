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


def get_user_command():
    printer.print_command_options()
    user_command = input("Please give a command:\n>>> ")
    printer.print_separator()

    return user_command

def evaluate_expression(validator: InputValidator, sy: ShuntingYard, rpn_evaluator: RPNEvaluator):  # pylint: disable=too-many-statements
    while True:
        print("\nGive a mathematical expression to evaluate ('h' help, 'c' cancel):")
        expression_input = input(">>> ")

        if expression_input == "c":
            return

        if expression_input == "h":
            printer.print_expression_help()

        else:
            try:
                validated_expression = validator.validate_expression(expression_input)
                # Variable the user wants to set e.g. "A"
                var_to_set = validated_expression[1]

                if var_to_set:
                    print("\nVariable to set:")
                    print(var_to_set)

                print("\nValidated tokens:")
                print(validated_expression[0])

            except InvalidExpressionException as e:
                print(f"\nValidation error: {e}")
                continue

            try:
                rpn_expression = sy.convert_to_rpn(validated_expression[0])
                print("\nReverse Polish Notation (RPN):")
                print(rpn_expression)

            except InvalidExpressionException as e:
                print(f"\nError when converting to RPN: {e}")
                continue

            try:
                end_result = rpn_evaluator.evaluate_rpn_expression(rpn_expression)
                print("\nFinal result:")
                print(end_result)

            except InvalidExpressionException as e:
                print(f"\nError when evaluating the RPN expression: {e}")
                continue

            if var_to_set:
                set_variable(var_to_set, end_result, validator)

            return

def set_variable(var_to_set: str, var_value: int | float, validator: InputValidator):
    while True:
        if var_to_set in USER_VARS:
            print(f"\nThe variable {var_to_set} already has a value. Do you want to "
                  "overwrite value? \n[y (yes) / n (no) / A-Z (to select new variable)]")
            command = input(">>> ")

            if command in string.ascii_uppercase:
                var_to_set = command
                continue

            if command == "y":
                break

            if command == "n":
                print("\nVariable not updated")
                return

            print("\nInvalid command. Please try again.")
            continue
        break

    try:
        USER_VARS.update({var_to_set: var_value})
        validator.update_user_variable(var_to_set, var_value)
        print(f"\nVariable {var_to_set} = {var_value} set!")
        return
    except (TypeError, ValueError) as e:
        raise InvalidExpressionException("Could not update variable.") from e

def main():
    validator = InputValidator(USER_VARS)
    sy = ShuntingYard()
    rpn_evaluator = RPNEvaluator()

    printer.print_intro()
    printer.print_instructions()
    print("\nWhat would you like to do next?")

    while True:
        user_command = get_user_command()

        if user_command == "q":
            print("\n*** Quitting the program. Bye! ***\n")
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
