import math
from .exceptions import InvalidExpressionException
"""
Checks validity of the user's input. Either accepts it and returns an optimal
form of the expression or gives an error
"""

class InputValidator():

    def __init__(self, user_variables):
        self.operators = set(["+", "-", "*", "/", "^", ])
        self.functions = set(["sin", "sqrt", "min", "max"])
        self.characters = set(["(", ")", "."])
        self.allowed_start_chars = set(["s", "m", "-", "(", "."])
        self.allowed_end_chars = set([")", "."])
        self.user_variables = user_variables
        self.bracket_equality = 0


    @staticmethod
    def validate_var_value(val_input: str):
        # Takes user provided number value of type str as input and returns it as int or float if valid
        valid_value = float(val_input)

        if valid_value.is_integer():
            valid_value = int(valid_value)

        return valid_value


    def validate_expression(self, user_expression:str):
        # Takes mathematical expression as input
        # Returns the expression as a list of tokens
        valid_tokens = []
        user_expression = user_expression.strip()

        # Validate length and first/last character
        self.validate_length(user_expression)
        self.validate_first_character(user_expression)
        self.validate_last_character(user_expression)

        # Iterate over expression and add valid tokens to valid_tokens list
        previous_char = user_expression[0]
        previous_type = type(previous_char)

        for i in range(1, len(user_expression)+1):
            pass


        return valid_tokens


    def validate_length(self, user_expression):
        if len(user_expression) < 3:
            raise InvalidExpressionException("The expression is too short")


    def validate_first_character(self, user_expression):
        first_char = user_expression[0]

        if not first_char.isdigit():
            if not first_char in self.user_variables:
                if not first_char in self.allowed_start_chars:
                    raise InvalidExpressionException("Invalid first character")


    def validate_last_character(self, user_expression):
        last_char = user_expression[-1]

        if not last_char.isdigit():
            if not last_char in self.user_variables:
                if not last_char in self.allowed_end_chars:
                    raise InvalidExpressionException("Invalid last character")
