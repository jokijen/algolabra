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
        self.allowed_start_chars = set(["c", "p", "s", "m", "(", ".", " "])
        self.allowed_end_chars = set(["i", ")", ".", " "])

    def update_user_variable(self, var_character: str, var_value: str):
        """Updates the dictionary self.user_variables with new variable (key-value pair).

        Args: 
        var_character -- a capital letter A-Z (key)
        var_value -- any value string (value)

        Returns: Nothing, but raises and exception with failure
        """
        self.user_variables.update({var_character: var_value})

    def validate_expression(self, user_expression: str) -> list:
        """Takes the user's mathematical expression as input. Checks if the user wants to define a
        variable. Removes spaces. Ensures the string is not empty and that first and last character
        are valid. Tokenises the string into a list of str type tokens. Checks for invalid characters
        that were not tokenised. Finally converts token list to a list of valid tokens.

        Args:
        user_expression -- user's mathematical expression

        Returns: A tuple containing the expression as list of valid tokens of type str or float and a
        variable to set or 'None' if none 
        """
        var_to_set = None

        spaceless_expression = self._remove_spaces(user_expression)

        if self._user_defines_variable(spaceless_expression):
            var_to_set = spaceless_expression[0]
            spaceless_expression = spaceless_expression[2:]

        self._validate_length(spaceless_expression)
        self._validate_first_and_last(spaceless_expression)

        # Tokenise the expression
        tokens = self._tokenise_expression(spaceless_expression)

        # Ensure there are no surplus characters that are not valid
        self._check_for_invalid_characters(spaceless_expression, tokens)

        validated_tokens = self._validate_tokens(tokens)

        return (validated_tokens, var_to_set)

    def _remove_spaces(self, user_expression: str) -> str:
        """Removes spaces from the expression by iterating through it and forming a new string from
        the non-space characters.

        Args: 
        user_expression -- the mathematical expression to remove spaces from

        Returns: A string containing the user_expression without spaces
        """
        spaceless_str = ""

        for char in user_expression:
            if char != " ":
                spaceless_str += char

        return spaceless_str

    def _user_defines_variable (self, user_expression: str) -> bool:
        """Checks if a user_expression starts with a capital ASCII letter followed by an equals sign
        (e.g. "A="), which would indicate that the user wants to set a value for a variable

        Args: 
        user_expression -- the mathematical expression to check

        Returns: True if the user wants to set a variable, False otherwise
        """
        if len(user_expression) >= 2:
            if user_expression[0] in string.ascii_uppercase:
                if user_expression[1] == "=":
                    return True
        return False

    def _expand_variable(self, token: str) -> float:
        """Expands any variable that has been set by the user and returns its value.

        Args: 
        token -- The string token containing an upper case ASCII letter to evaluate

        Returns: The value from the dictionary containing set variables (type str)
        """
        if not token in self.user_variables.keys():
            raise InvalidExpressionException(f"The variable {token} has not been defined!")

        var_value = self.user_variables[token]
        return float(var_value)

    def _validate_length(self, user_expression: str):
        """Ensures no empty strings will be accepted.

        Args:
        user_expression -- the mathematical expression to check

        Returns: Nothing if input not an empty string, raises exception otherwise
        """
        if len(user_expression) < 1:
            raise InvalidExpressionException("Empty expression!")

    def _validate_first_and_last(self, user_expression: str):
        """Validates the first and last characters in the expression by checking if they are numbers and
        comparing them to the allowed start/end characters.

        Args:
        user_expression -- the original mathematical expression to compare

        Returns: Nothing if first and last characters are valid or raises an exception otherwise
        """
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

    def _tokenise_expression(self, user_expression: str) -> list:
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
            | (?P<variable>[A-Z])       # Match variables A-Z
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

    def _check_for_invalid_characters(self, user_expression: str, tokens: list):
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

    def _validate_tokens(self, tokens: list) -> list:  # pylint: disable=too-many-statements
        """Takes the tokenised mathematical expression as input. Removes commas. Checks for: correctly
        paired brackets, no consecutive operators, correct number of args for two arg functions
        (max/min). Attaches unary negative to relevant number or converts it to "n" for clarity.
        Expands variables. Adds brackets to enclose both arguments of 'min'/'max'. Removes commas.

        Args:
        tokens -- A list of strings - tokenised version of the user's mathematical expression input

        Returns: A list of valid tokens of type str or float
        """
        validated_tokens = []
        bracket_equality = 0
        min_max_brackets_required = set()
        previous_is_neg = False
        expected_commas = 0

        for i, token in enumerate(tokens):
            if previous_is_neg:
                previous_is_neg = False  # The number token inspected was added in the last iteration
                continue

            bracket_equality += self._get_bracket_value(token)
            # Add a closing bracket for min/max if necessary
            if bracket_equality in min_max_brackets_required:
                validated_tokens.append(")")
                min_max_brackets_required.remove(bracket_equality)
            if bracket_equality < 0:
                raise InvalidExpressionException(
                    "Closing bracket before an opening bracket or too many closing brackets!"
                    )

            # Handle unary minus by attaching it to a number and adding the neg float to validated
            # tokens, or replacing the minus with "n" for negative, if in between brackets
            if token == "-":

                if i > 0 and validated_tokens[-1] == "(":
                    if self._is_number(tokens[i+1]):
                        validated_tokens.append(-float(tokens[i+1]))
                        previous_is_neg = True
                        continue

                    if tokens[i+1] in string.ascii_uppercase:
                        var_value = self._expand_variable(tokens[i+1])
                        validated_tokens.append(-var_value)
                        previous_is_neg = True
                        continue

                    if tokens[i+1] == "(":
                        token = "n"

            # Min/max arguments must be enclosed in brackets to ensure they are correctly calculated. This is
            # done by adding an opening bracket after 'min'/'max', adding closing and opening bracket when there
            # is a comma, and finally adding a closing bracket when the bracket equality is the same as in the start
            if token in ("max", "min"):
                min_max_brackets_required.add(bracket_equality) # Save the value requiring an extra closing bracket
                expected_commas += 1
                validated_tokens.append(token)
                validated_tokens.append("(")
                continue

            if token == ",":
                expected_commas -= 1
                validated_tokens.append(")")
                validated_tokens.append("(")
                continue

            # Ensure there are no consecutive operators
            if token in self.operators:
                if i > 0 and validated_tokens[-1] in self.operators:
                    raise InvalidExpressionException(
                        f"Consecutive operators not allowed!: '{validated_tokens[-1]}', '{token}'"
                        )

            # Expand variables and convert to floats
            if token in string.ascii_uppercase:
                var_value = self._expand_variable(token)
                validated_tokens.append(var_value)
                continue

            # Convert numbers to floats
            if self._is_number(token):
                validated_tokens.append(float(token))
                continue

            # Convert constants to floats
            if token in self.constants:
                validated_tokens.append(self.constants[token])
                continue

            validated_tokens.append(token)

        if bracket_equality != 0:
            raise InvalidExpressionException(f"Unequal brackets!: {bracket_equality}x closing bracket missing")
        if expected_commas < 0:
            raise InvalidExpressionException(
                "Unnecessary commas or too many arguments! " \
                "Use period '.' as the decimal separator and check any two argument functions"
                )
        if expected_commas > 0:
            raise InvalidExpressionException("Not enough commas! Check the two argument functions")

        return validated_tokens

    def _get_bracket_value(self, token: str) -> int:
        """Takes a token as input, checks if it is a left or right bracket and returns an int:
        1 for opening/left and -1 for closing/right barcket, or 0 if not a bracket.

        Args:
        token -- s token from the user's mathematical expression input

        Returns: An int value 1/-1/0 representing opening/closing/not bracket
        """
        if token == "(":
            return 1
        if token == ")":
            return -1
        return 0

    def _is_number(self, str_input: str) -> bool:
        """Checks if argument string contains a number e.g. '-3', '7.89'

        Args: 
        str_input -- string input to check

        Returns: True if str_input contains a valid number that can be converted into float,
        False otherwise
        """
        try:
            float(str_input)
            return True
        except ValueError:
            return False
