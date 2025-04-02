import unittest
from src.core.input_validator import InputValidator
from src.core.exceptions import InvalidExpressionException


class TestInputValidator(unittest.TestCase):
    def setUp(self):
        self.user_variables = {"A": 1.45, "Z": -8}
        self.validator = InputValidator(self.user_variables)

    def test_constructor_sets_user_variables_correctly(self):
        self.assertEqual(self.validator.user_variables, self.user_variables)
    
    def test_validate_var_value_decimal(self):
        result = self.validator.validate_var_value("4.5")
        self.assertEqual(result, 4.5)

    def test_validate_var_value_negative_integer(self):
        result = self.validator.validate_var_value("-3")
        self.assertEqual(result, -3)
    
    def test_validate_length_does_not_accept_too_short_input(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_length("-3")

    def test_validate_first_character_does_not_accept_invalid_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_first_character("*3+5.6")

    def test_validate_first_character_accepts_valid_character(self):
        try:
            self.validator.validate_first_character("(-3*32")
        except InvalidExpressionException:
            self.fail("validate_first_character raised an unnecessary exception")

    def test_validate_last_character_does_not_accept_invalid_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_last_character("12*13/")

    def test_validate_last_character_accepts_valid_character(self):
        try:
            self.validator.validate_last_character("5*32")
        except InvalidExpressionException:
            self.fail("validate_last_character raised an unnecessary exception")
