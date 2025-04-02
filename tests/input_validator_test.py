import unittest
from src.core.input_validator import InputValidator
from src.core.exceptions import InvalidExpressionException


class TestInputValidator(unittest.TestCase):
    def setUp(self):
        self.user_variables = {"A": "1.45", "H": "sqrt(9)*20", "Z": "-8"}
        self.validator = InputValidator(self.user_variables)

    def test_constructor_sets_user_variables_correctly(self):
        self.assertEqual(self.validator.user_variables, self.user_variables)

    def test_update_user_vars_updates_user_vars(self):
        new_variables = {"A": "1.45", "Z": "-8"}
        self.validator.update_user_vars(new_variables)
        self.assertEqual(new_variables, self.validator.user_variables)

    def test_validate_var_character_accepts_valid_char(self):
        result = self.validator.validate_var_character("Z")
        self.assertEqual(result, True)

    def test_validate_var_character_adoes_not_accept_small_ascii_char(self):
        result = self.validator.validate_var_character("z")
        self.assertEqual(result, False)

    def test_validate_var_character_adoes_not_accept_two_capital_ascii_chars(self):
        result = self.validator.validate_var_character("AA")
        self.assertEqual(result, False)

    def test_validate_var_character_adoes_not_accept_number(self):
        result = self.validator.validate_var_character("5")
        self.assertEqual(result, False)

    def test_validate_length_does_not_accept_too_short_input(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_length("-3")

    def test_validate_first_character_does_not_accept_invalid_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_first_character("*3+5.6")

    def test_validate_first_character_accepts_digit(self):
        try:
            self.validator.validate_first_character("3*32")
        except InvalidExpressionException:
            self.fail("validate_first_character raised an unnecessary exception")

    def test_validate_first_character_accepts_user_var(self):
        try:
            self.validator.validate_first_character("A+3*32")
        except InvalidExpressionException:
            self.fail("validate_first_character raised an unnecessary exception")

    def test_validate_first_character_accepts_allowed_start_character(self):
        try:
            self.validator.validate_first_character("(-3*32")
        except InvalidExpressionException:
            self.fail("validate_first_character raised an unnecessary exception")

    def test_validate_last_character_does_not_accept_invalid_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_last_character("12*13/")

    def test_validate_last_character_accepts_digit(self):
        try:
            self.validator.validate_last_character("5*32")
        except InvalidExpressionException:
            self.fail("validate_last_character raised an unnecessary exception")

    def test_validate_last_character_accepts_user_var(self):
        try:
            self.validator.validate_last_character("5*32-A")
        except InvalidExpressionException:
            self.fail("validate_last_character raised an unnecessary exception")

    def test_validate_last_character_accepts_allowed_end_character(self):
        try:
            self.validator.validate_last_character("5*32)")
        except InvalidExpressionException:
            self.fail("validate_last_character raised an unnecessary exception")

    def test_check_for_invalid_characters_succeeds_when_exp_matches_tokenised_exp(self):
        user_expression = "5.65*pi+sqrt(-9)**sin(4)"
        tokens = ['5.65', '*', 'pi', '+', 'sqrt', '(', '-', '9', ')', '**', 'sin', '(', '4', ')']
        try:
            self.validator.check_for_invalid_characters(user_expression, tokens)
        except InvalidExpressionException:
            self.fail("validate_last_character raised an unnecessary exception")

    def test_check_for_invalid_characters_fails_when_exp_not_matches_tokenised_exp(self):
        user_expression = "5.65*pi+sqrt(-9)**sin(4)"
        tokens = ['5.65', '*', 'pi', '+', 'sqrt', '(', '-', '9', ')', '**', 'sin', '(', '4']
        with self.assertRaises(InvalidExpressionException):
            self.validator.check_for_invalid_characters(user_expression, tokens)
