"""
Checks validity of the user's input. Either accepts it and returns an optimal
form of the expression or gives an error
"""

def validate_var_value(val_input):
    valid_value = float(val_input)

    if valid_value.is_integer():
        valid_value = int(valid_value)

    return valid_value
