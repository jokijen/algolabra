import math
import re
import string
from .exceptions import InvalidExpressionException
"""
Checks validity of the user's input. Either accepts it and returns an optimal
form of the expression or gives an error
"""

class InputValidator():
    """The class is used to validate the mathematical expression provided by
    the user and return the expression as a valid, tokenised list where each
    component of the epression (e.g. digit, operator) is a list element. 

    Methods:
    * update_user_vars:
    * validate_var_character:
    * validate_var_value:
    * validate_length:
    * validate_first_character:
    * validate_last_character:
    * check_for_invalid_characters:
    * 
    * tokenise_expression:
    * validate_expression:
    """

    def __init__(self, user_variables):
        self.user_variables = user_variables
        self.operators = set(["+", "-", "*", "/", "^", ])
        self.functions = set(["cos", "sin", "sqrt", "min", "max"])
        self.characters = set(["(", ")", "."])
        self.allowed_start_chars = set(["c", "s", "m", "-", "(", "."])
        self.allowed_end_chars = set([")", "."])
        self.bracket_equality = 0


    def update_user_vars(self, new_user_variables):
        self.user_variables = new_user_variables


    def validate_var_character(self, char_input: str) -> bool:
        # Checks if user provided character is a single uppercase letter A-Z and returns True/False
        if len(char_input) == 1: 
            if char_input in string.ascii_uppercase:
                return True

        return False


    def validate_var_value(self, val_input: str):
        # Takes user provided number value of type str as input and returns it as int or float if valid
        valid_value = float(val_input)

        if valid_value.is_integer():
            valid_value = int(valid_value)

        return valid_value


    def validate_length(self, user_expression:str):
        if len(user_expression) < 3:
            raise InvalidExpressionException("The expression is too short!")


    def validate_first_character(self, user_expression:str):
        first_char = user_expression[0]

        if not first_char.isdigit():
            if not first_char in self.user_variables:
                if not first_char in self.allowed_start_chars:
                    raise InvalidExpressionException("Invalid first character!")


    def validate_last_character(self, user_expression:str):
        last_char = user_expression[-1]

        if not last_char.isdigit():
            if not last_char in self.user_variables:
                if not last_char in self.allowed_end_chars:
                    raise InvalidExpressionException("Invalid last character!")


    def check_for_invalid_characters(self, user_expression:str, tokens:list):
        comparison_list = "".join(tokens)
        if len(user_expression) != len(comparison_list):
            raise InvalidExpressionException("The expression contains invalid characters!")


    def validate_used_variables(self, tokens:list):
        pass

    def tokenise_variables(self, tokens:list):
        pass


    def tokenise_expression(self, user_expression:str):
        # Takes mathematical expression as input
        # Returns the expression as a list of tokens
        tokens = []

        pattern = re.compile(r"""
            (?P<sign>[-])
            | (?P<float>\d+\.\d+)       # Match positive floats
            | (?P<integer>\d+\.?)       # Match positive integers
            | (?P<negative_sign>[,])    # Match the minus sign
            | (?P<varible>[A-Z])        # Match variables A-Z
            | (?P<constant>pi)          # Match constants
            | (?P<function>cos|sin|sqrt|min|max) # Match functions
            | (?P<operator>\*\*|[+\-*/]) # Match operators
            | (?P<parenthesis>[())])    # Match parenthesis
            | (?P<comma>[,])            # Match commas
            | (?P<whitespace>\s+)       # Match whitespaces
        """, re.VERBOSE)

        tokens = pattern.findall(user_expression)
        token_list = [token for group in tokens for token in group if token]

        # Validate variables used in the exression and convert them into tokens
        #self.validate_used_variables(token_list)
        #self.tokenise_variables(token_list)

        self.check_for_invalid_characters(user_expression, token_list)
        
        return token_list


    def validate_expression(self, user_expression:str):
        # Takes mathematical expression as input
        # Returns the expression as a list of valid tokens

        # Validate length and first/last character
        self.validate_length(user_expression)
        self.validate_first_character(user_expression)
        self.validate_last_character(user_expression)

        #Tokenise the expression
        valid_tokens = self.tokenise_expression(user_expression)

        # w_tokens = self.validate_used_variables(w)
        # x_tokens = self.check_operator_validity(x)
        # y_tokens = self.check_brackets(y)
        # z_tokens = self.check_digits(z)

        return valid_tokens
