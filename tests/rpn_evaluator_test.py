import unittest
from src.core.rpn_evaluator import RPNEvaluator
from src.core.queue import Queue
from src.core.exceptions import InvalidExpressionException


class TestRPNEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = RPNEvaluator()

    def test_addition(self):
        tokens = Queue()
        tokens.enqueue(30.0)
        tokens.enqueue(15.5)
        tokens.enqueue('+')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(45.5, result)

    def test_subtraction(self):
        tokens = Queue()
        tokens.enqueue(-10.0)
        tokens.enqueue(10.0)
        tokens.enqueue('-')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(-20, result)

    def test_multiplication(self):
        tokens = Queue()
        tokens.enqueue(2.0)
        tokens.enqueue(3.6)
        tokens.enqueue('*')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(7.2, result)

    def test_division_with_valid_operands_accepted(self):
        tokens = Queue()
        tokens.enqueue(30.0)
        tokens.enqueue(2.0)
        tokens.enqueue('/')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(15, result)

    def test_division_with_zero_not_accepted(self):
        tokens = Queue()
        tokens.enqueue(30.0)
        tokens.enqueue(0.0)
        tokens.enqueue('/')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_exponentiation(self):
        tokens = Queue()
        tokens.enqueue(30.0)
        tokens.enqueue(0.0)
        tokens.enqueue('**')
        result = self.evaluator.evaluate_rpn_expression(tokens)
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
        tokens = Queue()
        tokens.enqueue(9.0)
        tokens.enqueue('sqrt')
        result = self.evaluator.evaluate_rpn_expression(tokens)
        self.assertEqual(3, result)

    def test_square_root_of_negative_not_accepted(self):
        tokens = Queue()
        tokens.enqueue(-9.0)
        tokens.enqueue('sqrt')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

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

    def test_no_tokens(self):
        tokens = Queue()
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_unrecognised_token(self):
        tokens = Queue()
        tokens.enqueue('b')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_not_enough_operands_for_operator(self):
        tokens = Queue()
        tokens.enqueue(1.0)
        tokens.enqueue('+')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_not_enough_operands_for_one_arg_function(self):
        tokens = Queue()
        tokens.enqueue('sqrt')
        with self.assertRaises(InvalidExpressionException):
            self.evaluator.evaluate_rpn_expression(tokens)

    def test_not_enough_operands_for_two_arg_function(self):
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
