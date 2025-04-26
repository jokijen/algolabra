import unittest
from src.core.input_validator import InputValidator
from src.core.exceptions import InvalidExpressionException


class TestInputValidator(unittest.TestCase):
    def setUp(self):
        self.user_variables = {
            "A": 1.45,
            "B": 20,
            "Z": -8
            }
        self.validator = InputValidator(self.user_variables)

    def test_constructor_sets_user_variables_correctly(self):
        self.assertEqual(self.validator.user_variables, self.user_variables)

    def test_update_user_vars_updates_user_vars(self):
        new_var_char = "A"
        new_var_input = "45"
        self.validator.update_user_vars(new_var_char, new_var_input)
        self.assertEqual(self.validator.user_variables["A"], "45")

    def test_is_number_identifies_float(self):
        result = self.validator._is_number("5.7")
        self.assertTrue(result)

    def test_is_number_identifies_neg_int(self):
        result = self.validator._is_number("-9")
        self.assertTrue(result)

    def test_is_number_does_not_identify_function_with_number(self):
        result = self.validator._is_number("sqrt(3)")
        self.assertFalse(result)

    def test_is_number_does_not_identify_expression(self):
        result = self.validator._is_number("3+3")
        self.assertFalse(result)

    def test_expand_variable_correctly_expands_variable(self):
        result = self.validator._expand_variable("A")
        self.assertEqual(result, 1.45)

    def test_validate_length_does_not_accept_too_short_input(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_length("")

    def test_validate_first_and_last_accepts_both_are_digits(self):
        try:
            self.validator._validate_first_and_last("3*32")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_accepts_both_are_user_vars(self):
        try:
            self.validator._validate_first_and_last("A+3*32*B")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_accepts_allowed_start_end_chars(self):
        try:
            self.validator._validate_first_and_last("(-3)*(32+2)")
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_validate_first_and_last_does_not_accept_invalid_first_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_first_and_last("*3+5.6")

    def test_validate_first_and_last_does_not_accept_invalid_last_character(self):
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_first_and_last("12*13/")

    def test_check_for_invalid_characters_succeeds_when_exp_matches_tokenised_exp(self):
        user_expression = "5.65*pi+sqrt(-9)**sin(4)"
        tokens = ['5.65', '*', 'pi', '+', 'sqrt', '(', '-', '9', ')', '**', 'sin', '(', '4', ')']
        try:
            self.validator._check_for_invalid_characters(user_expression, tokens)
        except InvalidExpressionException:
            self.fail("validate_first_and_last raised an unnecessary exception")

    def test_check_for_invalid_characters_fails_when_exp_and_tokens_do_not_match(self):
        user_expression = "5.65*pi+sqrt(-9)**sin(4)"
        tokens = ['5.65', '*', 'pi', '+', 'sqrt', '(', '-', '9', ')', '**', 'sin', '(', '4']
        with self.assertRaises(InvalidExpressionException):
            self.validator._check_for_invalid_characters(user_expression, tokens)

    def test_tokenise_expression_correctly_tokenises_str(self):
        user_expression = "12*0.6/5**(-2)+sqrt(90)-min(sin(10), 5)"
        tokens = ['12', '*', '0.6', '/', '5', '**', '(', '-', '2', ')', '+', 'sqrt', '(',
                  '90', ')', '-', 'min', '(', 'sin', '(', '10', ')', ',', ' ', '5', ')']
        result = self.validator._tokenise_expression(user_expression)
        self.assertEqual(result, tokens)

    def test_bracket_value_identifies_left_bracket(self):
        result = self.validator._get_bracket_value("(")
        self.assertEqual(result, 1)

    def test_bracket_value_identifies_right_bracket(self):
        result = self.validator._get_bracket_value(")")
        self.assertEqual(result, -1)

    def test_bracket_value_identifies_non_bracket_character(self):
        result = self.validator._get_bracket_value(",")
        self.assertEqual(result, 0)

    def test_validate_expression_accepts_valid_expression(self):
        user_expression = "A+(-3)*A**2.5"
        tokenised = [1.45, '+', '(', -3.0, ')', '*', 1.45, '**', 2.5]
        result = self.validator.validate_expression(user_expression)
        self.assertEqual(result, (tokenised, None))

    def test_validate_expression_accepts_valid_short_expression(self):
        user_expression = "A"
        tokenised = [1.45]
        result = self.validator.validate_expression(user_expression)
        self.assertEqual(result, (tokenised, None))

    def test_validate_expression_accepts_valid_short_expression2(self):
        user_expression = "(-A)+5+pi"
        tokenised = ['(', -1.45, ')', '+', 5.0, '+', 3.141592653589793]
        result = self.validator.validate_expression(user_expression)
        self.assertEqual(result, (tokenised, None))

    def test_validate_expression_sets_variable(self):
        user_expression = "L = (-9)**3"
        variable = "L"
        tokenised = ['(', -9.0, ')', '**', 3.0]
        result = self.validator.validate_expression(user_expression)
        self.assertEqual(result, (tokenised, variable))

    def test_validate_expression_does_not_accept_undefined_variable(self):
        user_expression = "(-3)*Y**2.5"
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_expression(user_expression)

    def test_validate_expression_does_not_accept_consecutive_operators(self):
        user_expression = "(-3)***2.5"
        with self.assertRaises(InvalidExpressionException):
            self.validator.validate_expression(user_expression)

    def test_validate_tokens_does_not_accecpt_too_many_commas(self):
        token_input = ['min', '(','1', ',', '2', ',', '3', ')']
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_tokens(token_input)

    def test_validate_tokens_does_not_accecpt_too_few_commas(self):
        token_input = ['min', '(','1', '3', ')']
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_tokens(token_input)

    def test_validate_tokens_does_not_accecpt_right_bracket_first(self):
        token_input = ['1', '+', ')', '1', '+', '3', '(']
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_tokens(token_input)

    def test_validate_tokens_does_not_accecpt_unequal_brackets(self):
        token_input = ['1', '+', '(', '-', '5', ')', '+', '3', '(']
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_tokens(token_input)

    def test_validate_tokens_does_not_accecpt_unary_neg_missing_brackets(self):
        token_input = ['min', '(', '9', ',', '-', '8', ')']
        with self.assertRaises(InvalidExpressionException):
            self.validator._validate_tokens(token_input)

    def test_validate_tokens_converts_unary_neg_to_n(self):
        token_input = ['1', '+', '(', '-', '(', '3', '+', '3', ')', ')']
        tokenised = [1, '+', '(', 'n', '(', 3.0, '+', 3, ')', ')']
        result = self.validator._validate_tokens(token_input)
        self.assertEqual(result, tokenised)
