import unittest
from src.core.rpn_evaluator import RPNEvaluator
from src.core.queue import Queue
from src.core.exceptions import InvalidExpressionException


class TestRPNEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = RPNEvaluator()

    def test_addition(self):
        result = self.evaluator._apply_operation('+', 30.0, 15.5)
        self.assertEqual(45.5, result)

    def test_subtraction(self):
        result = self.evaluator._apply_operation('-', -10.0, 10.0)
        self.assertEqual(-20, result)

    def test_multiplication(self):
        result = self.evaluator._apply_operation('*', 2.0, 3.6)
        self.assertEqual(7.2, result)

    def test_division_with_valid_operands_accepted(self):
        result = self.evaluator._apply_operation('/', 30.0, 2.0)
        self.assertEqual(15, result)

    def test_division_with_zero_not_accepted(self):
        with self.assertRaises(InvalidExpressionException):
            self.evaluator._apply_operation('/', 8.0, 0.0)

    def test_exponentiation(self):
        result = self.evaluator._apply_operation('**', 20.0, 0.0)
        self.assertEqual(1, result)

    def test_unary_negation(self):
        tokens = Queue()
        tokens.enqueue(10.0)
        tokens.enqueue(2.5)
        tokens.enqueue('n')
        tokens.enqueue('+')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(7.5, result)

    def test_cosine_in_degrees(self):
        tokens = Queue()
        tokens.enqueue(60.0)
        tokens.enqueue('cos')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(0.5, result)

    def test_sine_in_degrees(self):
        tokens = Queue()
        tokens.enqueue(90.0)
        tokens.enqueue('sin')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(1, result)

    def test_square_root_of_positive_accepted(self):
        result = self.evaluator._apply_operation('sqrt', None, 9.0)
        self.assertEqual(3, result)

    def test_square_root_of_negative_not_accepted(self):
        with self.assertRaises(InvalidExpressionException):
            self.evaluator._apply_operation('sqrt', None, -9.0)

    def test_min_with_first_arg_min(self):
        tokens = Queue()
        tokens.enqueue(-20.0)
        tokens.enqueue(20.0)
        tokens.enqueue('min')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(-20, result)

    def test_min_with_second_arg_min(self):
        tokens = Queue()
        tokens.enqueue(100.0)
        tokens.enqueue(1000.0)
        tokens.enqueue('min')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(100, result)

    def test_max_with_first_arg_max(self):
        tokens = Queue()
        tokens.enqueue(100.0)
        tokens.enqueue(1000.0)
        tokens.enqueue('max')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(1000, result)

    def test_max_with_second_arg_max(self):
        tokens = Queue()
        tokens.enqueue(-20.0)
        tokens.enqueue(20.0)
        tokens.enqueue('max')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(20, result)

    # sqrt(3*3)*3**2.5+sin(51/2+25.5)-cos(51/2+25.5)/max(1+1,0)*(-1)
    def test_complex_expression(self):
        tokens = Queue()
        tokens.enqueue(3.0)
        tokens.enqueue(3.0)
        tokens.enqueue('*')
        tokens.enqueue('sqrt')
        tokens.enqueue(3.0)
        tokens.enqueue(2.5)
        tokens.enqueue('**')
        tokens.enqueue('*')
        tokens.enqueue(51.0)
        tokens.enqueue(2.0)
        tokens.enqueue('/')
        tokens.enqueue(25.5)
        tokens.enqueue('+')
        tokens.enqueue('sin')
        tokens.enqueue('+')
        tokens.enqueue(51.0)
        tokens.enqueue(2.0)
        tokens.enqueue('/')
        tokens.enqueue(25.5)
        tokens.enqueue('+')
        tokens.enqueue('cos')
        tokens.enqueue(1.0)
        tokens.enqueue(1.0)
        tokens.enqueue('+')
        tokens.enqueue(0.0)
        tokens.enqueue('max')
        tokens.enqueue('/')
        tokens.enqueue(-1.0)
        tokens.enqueue('*')
        tokens.enqueue('-')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(47.8571779613, result)

    def test_no_tokens(self):
        tokens = Queue()
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_unrecognised_token(self):
        tokens = Queue()
        tokens.enqueue('b')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_insufficient_operands_for_operator(self):
        tokens = Queue()
        tokens.enqueue(1.0)
        tokens.enqueue('+')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_insufficient_operands_for_one_arg_function(self):
        tokens = Queue()
        tokens.enqueue('sqrt')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_insufficient_operands_for_two_arg_function(self):
        tokens = Queue()
        tokens.enqueue(1.0)
        tokens.enqueue('min')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_overflow_error_operator(self):
        tokens = Queue()
        tokens.enqueue(90000.0)
        tokens.enqueue(90000.0)
        tokens.enqueue('**')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_too_many_items_left_in_stack(self):
        tokens = Queue()
        tokens.enqueue(1.0)
        tokens.enqueue(1.0)
        tokens.enqueue(1.0)
        tokens.enqueue('+')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)
