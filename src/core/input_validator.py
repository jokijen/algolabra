"""Checks validity of the user's input string. The string is either considered
valid and returned tokenised (list) or an error is triggered
"""
import math
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
        self.constants = {"pi": math.pi}
        self.operators = set(["+", "-", "*", "/", "**"])
        #self.functions = set(["cos", "sin", "sqrt", "min", "max"])
        #self.characters = set(["(", ")", "."])
        self.allowed_start_chars = set(["c", "p", "s", "m", "(", "."])
        self.allowed_end_chars = set(["i", ")", "."])


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
        string_from_tokens = "".join(tokens)
        if user_expression != string_from_tokens:
            raise InvalidExpressionException("The expression contains invalid characters!")


    def tokenise_expression(self, user_expression: str) -> list:
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


    def get_bracket_value(self, token: str) -> int:
        if token == "(":
            return 1
        if token == ")":
            return -1
        return 0


    def validate_tokens(self, tokens: list) -> list:
        """Takes the tokenised mathematical expression as input. Removes: spaces and commas.
        Checks for: correctly paired brackets, no consecutive operators, correct number of
        args for two arg functions (max/min). Attaches unary negative to relevant number or
        converts it to "n" for clarity. 
               
        Args: 
        tokens -- tokenised version of the user's mathematical expression input
        
        Returns: A list of valid tokens of type str or float
        """
        validated_tokens = []
        bracket_equality = 0
        previous_is_neg = False
        expected_commas = 0

        for i, token in enumerate(tokens):
            if previous_is_neg:
                previous_is_neg = False # The number was added in the last iteration
                continue

            if token == " ":
                continue

            if token == ",":
                expected_commas -= 1

            bracket_equality += self.get_bracket_value(token)
            if bracket_equality < 0:
                raise InvalidExpressionException("Closing bracket before an opening bracket!")

            if token in ("max", "min"):
                expected_commas += 1

            # Handle unary minus by attaching it to a number and adding the neg float to validated
            # tokens, or replacing the minus with "n" for negative, if in between brackets
            if token == "-":
                if i > 0 and validated_tokens[-1] == "(":
                    if self.is_number(tokens[i+1]):
                        validated_tokens.append(-float(tokens[i+1]))
                        previous_is_neg = True
                        continue

                    if tokens[i+1] == "(" or tokens[i+1:i+2] == " (":
                        token = "n"
                if i > 0 and validated_tokens[-1] == ",":
                    raise InvalidExpressionException(
                        f"Unary negative missing brackets!: '{tokens[i]+tokens[i+1]}'"
                        )

            # Convert numbers to floats
            if self.is_number(token):
                validated_tokens.append(float(token))

            # Convert constants to floats
            elif token in self.constants:
                validated_tokens.append(self.constants[token])

            # Ensure there are no consecutive operators
            elif token in self.operators:
                if i > 0 and validated_tokens[-1] in self.operators:
                    raise InvalidExpressionException(
                        f"Consecutive operators not allowed!: '{validated_tokens[-1]}', '{token}'"
                        )
                validated_tokens.append(token)
            else:
                validated_tokens.append(token)

            # check brackets enclose neg no.
            # check functions have correct params

        if bracket_equality != 0:
            raise InvalidExpressionException("Unequal brackets!")
        if expected_commas < 0:
            raise InvalidExpressionException("Unnecessary commas! Check the two argument functions")
        if expected_commas > 0:
            raise InvalidExpressionException("Not enough commas! Check the two argument functions")

        return validated_tokens


    def validate_expression(self, user_expression: str) -> list:
        """Takes the user's mathematical expression as input. Expands all variables used (and
        recursively) variables in the variables). Ensures the string is not empty and that first
        and last character are valid. Tokenises the string into a list of str type tokens. Checks
        for invalid characters that were not tokenised. Finally converts token list to a list of
        valid tokens.
               
        Args: 
        user_expression -- user's mathematical expression
        
        Returns: The expression as list of valid tokens of type str or float
        """
        expanded_expression = self.expand_variables(user_expression)
        print("Expanded expression:", expanded_expression)

        self.validate_length(expanded_expression)
        self.validate_first_and_last(expanded_expression)

        # Tokenise the expression
        tokens = self.tokenise_expression(expanded_expression)

        # Ensure there are no surplus characters that are not valid
        self.check_for_invalid_characters(expanded_expression, tokens)

        validated_tokens = self.validate_tokens(tokens)

        return validated_tokens
