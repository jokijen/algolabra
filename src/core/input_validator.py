"""Checks validity of the user's input string. The string is either considered
valid and returned tokenised (list) or an error is triggered
"""
import re
import string
from .exceptions import InvalidExpressionException


class InputValidator:
    """The class is used to validate the mathematical expression provided by the user and return
    the expression as a valid, tokenised list where each component of the epression (e.g. digit,
    operator) is a list element of type str. 

    Attrs:
    user_variables -- A dictionary containing the variables A-Z that the user has set some value for
    """
    def __init__(self, user_variables: dict):
        self.user_variables = user_variables
        self.operators = set(["+", "-", "*", "/", "**"])
        #self.functions = set(["cos", "sin", "sqrt", "min", "max"])
        #self.characters = set(["(", ")", "."])
        self.allowed_start_chars = set(["c", "s", "m", "(", "."])
        self.allowed_end_chars = set([")", "."])


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


    def expand_variables(self, user_expression: str, recursion_depth=0) -> str:
        """Expands any variables used in the expression, and recursively expands any variables
        used in the value of an inspected variable.

        Args: 
        user_expression -- the mathematical expression to check for variables
        recursion_depth -- a counter used when limiting recursion depth and detecting circular
        references in the variables (default 0)
        
        Returns: An expanded expression with no more variables to expand
        """
        expanded_expression = ""

        if recursion_depth > 24:
            raise InvalidExpressionException("Circular reference for variable!")

        for char in user_expression:
            if char in string.ascii_uppercase:
                if not char in self.user_variables.keys():
                    raise InvalidExpressionException("The variable {char} has not been defined!")

                var_value = self.user_variables[char]

                # Check variable string for any variables.
                expanded_var = self.expand_variables(var_value, recursion_depth + 1)
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
        """Chacks for invalid characters by comparing the original expression string to a parsed
        (to string) version of the token list.
        
        Args: 
        user_expression -- the original mathematical expression to compare
        tokens -- the token list formed of the original mathematical expression
        
        Returns: Nothing if no invalid characters are present or raises an exception if they are
        """
        comparison_list = "".join(tokens)
        if len(user_expression) != len(comparison_list):
            raise InvalidExpressionException("The expression contains invalid characters!")


    def tokenise_expression(self, user_expression: str):
        """Takes a mathematical expression and uses regex to identify allowed characters/patterns
        in it, which is used to tokenise the founc elements.
                
        Args: 
        user_expression -- the original mathematical expression to compare
        
        Returns: The expression as list of str tokens
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
            | (?P<bracket>[())])        # Match brackets
            | (?P<comma>[,])            # Match commas
            | (?P<whitespace>\s+)       # Match whitespaces
        """, re.VERBOSE)

        tokens = pattern.findall(user_expression)
        token_list = [token for group in tokens for token in group if token]

        return token_list


    def get_bracket_value(self, token: str):
        if token == "(":
            return 1
        if token == ")":
            return -1
        return 0


    def validate_expression(self, user_expression: str):
        """Takes mathematical expression as input
        Returns the expression as a list of valid tokens
        """
        expanded_expression = self.expand_variables(user_expression)
        print("Expanded expression:", expanded_expression)

        self.validate_length(expanded_expression)
        self.validate_first_and_last(expanded_expression)

        # Tokenise the expression
        tokens = self.tokenise_expression(expanded_expression)

        # Ensure there are no surplus characters that are not valid
        self.check_for_invalid_characters(expanded_expression, tokens)

        validated_tokens = []
        i = 0
        bracket_equality = 0

        while i < len(tokens):
            previous = tokens[i-1] if i-1 >= 0 else None
            current = tokens[i]
            next = tokens[i+1] if i+1 < len(tokens) else None
            # print(validated_tokens)
            # print("Prev, curr, next:", previous, current, next)

            if current == " ":
                i += 1
                continue

            bracket_equality += self.get_bracket_value(current)
            if bracket_equality < 0:
                raise InvalidExpressionException("Closing bracket before an opening bracket!")

            # Handle unary minus, by attaching it to the number or replacing it with "n" for negative
            if current == "-":
                if previous == "(" and self.is_number(next):
                    validated_tokens.append(f"-{next}")
                    # print(f"Appended: -{next}")
                    i += 2
                    continue

                if previous == "(" and next == "(":
                    current = "n"


            # Check for consecutive operators e.g. ***


            validated_tokens.append(current)
            # print("Appended:", current)
            i += 1

        if bracket_equality != 0:
            raise InvalidExpressionException("Unequal brackets!")


        return validated_tokens
