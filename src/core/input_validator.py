"""Checks validity of the user's input string. The string is either considered
valid and returned tokenised (list) or an error is triggered
"""
import re
import string
from .exceptions import InvalidExpressionException


class InputValidator:
    """The class is used to validate the mathematical expression provided by
    the user and return the expression as a valid, tokenised list where each
    component of the epression (e.g. digit, operator) is a list element. 

    Methods:
    * update_user_vars: Updates the user variables of the object (arg: up-to-date variable dict)
    * validate_var_character: Validates that the str the user is trying to set is a capital letter A-Z
    * is_number: Checks if a str input can be converted into a float
    * validate_length: Validates lenght of the str input given by user and returns error if empty str
    * validate_first_and_last: Returns an error if first/last character is not avalid start/end character 
    * check_for_invalid_characters:
    * tokenise_expression:
    * validate_expression:
    """

    def __init__(self, user_variables: dict):
        self.user_variables = user_variables
        self.operators = set(["+", "-", "*", "/", "^", ])
        self.functions = set(["cos", "sin", "sqrt", "min", "max"])
        self.characters = set(["(", ")", "."])
        self.allowed_start_chars = set(["c", "s", "m", "-", "(", "."])
        self.allowed_end_chars = set([")", "."])
        self.bracket_equality = 0


    def update_user_vars(self, new_user_variables: dict):
        self.user_variables = new_user_variables


    def validate_var_character(self, char_input: str) -> bool:
        # Checks if user provided character is a single uppercase letter A-Z and returns True/False
        if len(char_input) == 1:
            if char_input in string.ascii_uppercase:
                return True

        return False


    def is_number(self, var_value: str) -> bool:
        try:
            float(var_value)
            return True
        except ValueError:
            return False


    def expand_variables(self, user_expression: str, seen=None) -> str:
        expanded_expression = ""
        if seen is None:
            seen = set()

        for char in user_expression:
            if char in string.ascii_uppercase:
                if not char in self.user_variables.keys():
                    raise InvalidExpressionException("The variable {char} has not been defined!")
                if char in seen:
                    raise InvalidExpressionException("Circular reference for variable!")
                
                seen.add(char)
                var_value = self.user_variables[char]
                if self.is_number(var_value):
                    expanded_expression += var_value # expanded_var is a number and does not require brackets
                else:
                    expanded_var = self.expand_variables(var_value, seen) # Recursively checks if variable contains other variables
                    expanded_expression += "(" + expanded_var + ")"
            else:
                expanded_expression += char
        return expanded_expression


    def validate_length(self, user_expression: str):
        if len(user_expression) < 1:
            raise InvalidExpressionException("Empty expression!")


    def validate_first_and_last(self, user_expression: str):
        first_char = user_expression[0]
        last_char = user_expression[-1]

        if not first_char.isdigit():
            if not first_char in self.user_variables:
                if not first_char in self.allowed_start_chars:
                    raise InvalidExpressionException("Invalid first character!")

        if not last_char.isdigit():
            if not last_char in self.user_variables:
                if not last_char in self.allowed_end_chars:
                    raise InvalidExpressionException("Invalid last character!")


    def check_for_invalid_characters(self, user_expression: str, tokens: list):
        comparison_list = "".join(tokens)
        if len(user_expression) != len(comparison_list):
            raise InvalidExpressionException("The expression contains invalid characters!")


    def tokenise_expression(self, user_expression: str):
        """Takes mathematical expression as input
        Returns the expression as a list of tokens
        """
        tokens = []

        pattern = re.compile(r"""
            (?P<sign>[-])
            | (?P<float>\d*\.\d+)       # Match positive floats
            | (?P<integer>\d+\.?)       # Match positive integers
            | (?P<negative_sign>[,])    # Match the minus sign
            | (?P<variable>[A-Z])       # Match variables A-Z # REMOVE
            | (?P<constant>pi)          # Match constants
            | (?P<function>cos|sin|sqrt|min|max) # Match functions
            | (?P<operator>\*\*|[+\-*/]) # Match operators
            | (?P<parenthesis>[())])    # Match parenthesis
            | (?P<comma>[,])            # Match commas
            | (?P<whitespace>\s+)       # Match whitespaces
        """, re.VERBOSE)

        tokens = pattern.findall(user_expression)
        token_list = [token for group in tokens for token in group if token]

        return token_list


    def validate_expression(self, user_expression: str):
        """Takes mathematical expression as input
        Returns the expression as a list of valid tokens
        """
        expanded_expression = self.expand_variables(user_expression)

        self.validate_length(expanded_expression)
        self.validate_first_and_last(expanded_expression)

        # Tokenise the expression
        tokens = self.tokenise_expression(expanded_expression)
        # Ensure there are no surplus characters that are not valid
        self.check_for_invalid_characters(expanded_expression, tokens)

        
        # x_tokens = self.check_operator_validity(x)
        # y_tokens = self.check_brackets(y)
        # z_tokens = self.check_digits(z)

        return tokens
