import unittest
from src.core.input_validator import InputValidator
from src.core.exceptions import InvalidExpressionException


class TestInputValidator(unittest.TestCase):
    def setUp(self):
        self.user_variables = {"A": "1.45", "B": "sqrt(9)*20", "C": "1+D", "D": "C+1", "Z": "-8"}
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

    def test_is_number_identifies_float(self):
        result = self.validator.is_number("-5.7")
        self.assertEqual(result, True)

    def test_is_number_identifies_neg_int(self):
        result = self.validator.is_number("9")
        self.assertEqual(result, True)

    def test_is_number_does_not_identify_letter(self):
        result = self.validator.is_number("sqrt(3)")
        self.assertEqual(result, False)

    def test_is_number_does_not_identify_expression(self):
        result = self.validator.is_number("sqrt(3)")
        self.assertEqual(result, False)

    def test_validate_length_does_not_accept_too_short_input(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_length("")

    def test_validate_first_and_last_does_not_accept_invalid_first_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_first_and_last("*3+5.6")

    def test_validate_first_and_last_accepts_first_is_digit(self):
        try:
            self.validator.validate_first_and_last("3*32")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_accepts_first_is_user_var(self):
        try:
            self.validator.validate_first_and_last("A+3*32")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_accepts_allowed_start_character(self):
        try:
            self.validator.validate_first_and_last("(-3*32")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_does_not_accept_invalid_last_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_first_and_last("12*13/")

    def test_validate_first_and_last_accepts_last_is_digit(self):
        try:
            self.validator.validate_first_and_last("5*32")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_accepts_last_is_user_var(self):
        try:
            self.validator.validate_first_and_last("5*32-A")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_accepts_allowed_end_character(self):
        try:
            self.validator.validate_first_and_last("5*32)")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_check_for_invalid_characters_succeeds_when_exp_matches_tokenised_exp(self):
        user_expression = "5.65*pi+sqrt(-9)**sin(4)"
        tokens = ['5.65', '*', 'pi', '+', 'sqrt', '(', '-', '9', ')', '**', 'sin', '(', '4', ')']
        try:
            self.validator.check_for_invalid_characters(user_expression, tokens)
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_check_for_invalid_characters_fails_when_exp_not_matches_tokenised_exp(self):
        user_expression = "5.65*pi+sqrt(-9)**sin(4)"
        tokens = ['5.65', '*', 'pi', '+', 'sqrt', '(', '-', '9', ')', '**', 'sin', '(', '4']
        with self.assertRaises(InvalidExpressionException):
            self.validator.check_for_invalid_characters(user_expression, tokens)

    def test_validate_expression_accepts_valid_expression(self):
        user_expression = "-3*A**2.5"
        tokenised = ['-', '3', '*', '1.45', '**', '2.5']
        result = self.validator.validate_expression(user_expression)
        self.assertEqual(result, tokenised)

    def test_validate_expression_does_not_accept_undefined_variable(self):
        user_expression = "-3*Y**2.5"
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_expression(user_expression)

    def test_validate_expression_does_not_accept_circular_variable(self):
        user_expression = "-3*C**2.5"
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_expression(user_expression)

    def test_expand_variables_correctly_expands_expression_in_var(self):
        user_expression = "-3*B**2.5"
        tokenised = ['-', '3', '*', '(', 'sqrt', '(', '9', ')', '*', '20', ')', '**', '2.5']
        result = self.validator.validate_expression(user_expression)
        self.assertEqual(result, tokenised)
