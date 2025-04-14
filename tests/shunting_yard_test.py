import unittest
from src.core.shunting_yard import ShuntingYard
from src.core.queue import Queue
from src.core.exceptions import InvalidExpressionException


class TestShuntingYard(unittest.TestCase):
    def setUp(self):
        self.shunting_yard = ShuntingYard()

    def test_convert_to_rpn(self):
        token_list = [
            2.0, '+', '(', -2.0, ')', '*', '(', 'n', '(', 'sqrt', '(',
            9.0, ')', ')', ')', '+', 'min', '(', 5.0, ',', 1.0, ')'
            ]
        
        rpn_queue = Queue()
        rpn_queue.enqueue(2.0)
        rpn_queue.enqueue(-2.0)
        rpn_queue.enqueue(9.0)
        rpn_queue.enqueue("sqrt")
        rpn_queue.enqueue("n")
        rpn_queue.enqueue("*")
        rpn_queue.enqueue("+")
        rpn_queue.enqueue(5.0)
        rpn_queue.enqueue(1.0)
        rpn_queue.enqueue("min")
        rpn_queue.enqueue("+")

        result = self.shunting_yard.convert_to_rpn(token_list)
        self.assertEqual(repr(result), repr(rpn_queue))

    def test_empty_input(self):
        token_list = []
        with self.assertRaises(InvalidExpressionException):
            self.shunting_yard.convert_to_rpn(token_list)
