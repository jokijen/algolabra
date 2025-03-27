"""
Checks validity of the user's input. Either accepts it and returns an optimal
form of the expression or gives an error
"""

def validate_var_value(val_input: str):
    # Takes user provided number value of type str as input and returns it as int or float if valid

    valid_value = float(val_input)

    if valid_value.is_integer():
        valid_value = int(valid_value)

    return valid_value


class InputValidator():

    def __init__(self, user_variables):
        self.operators = set(["+", "-", "*", "/", "^", ])
        self.functions = set(["sin", "sqrt", "min", "max"])
        self.characters = set(["(", ")", "."])
        self.variables = user_variables
        self.bracket_equality = 0

    def validate(self, user_input:str):
        pass

    def validate_first_and_last(self, character, first: bool):
        pass
