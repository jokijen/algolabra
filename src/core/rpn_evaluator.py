"""The PRN evaluator used for evaluating a RPN/postfix notation mathematical expression.
"""
import math
from .stack import Stack
from .queue import Queue
from .exceptions import InvalidExpressionException

class RPNEvaluator:
    """The class implements an evaluator for an RPN/postfix mathematical expression and returns
    the end result for the calculation.

    Attributes:
        operators (set): A set containing the allowed operators for the calculations
        one_arg_functions (set): A set containing the allowed one-argument functions for the calculations
        two_arg_functions (set): A set containing the allowed two-argument functions for the calculations

    Methods:
        evaluate_rpn_expression (tokens): Converts tokens (Queue object) forming an infix expression into RPN/postfix
        apply_operator (function, operand1, operand2):
        apply_one_arg_function (function, operand):
        apply_two_arg_function (function, operand1, operand2):
    """
    def __init__(self):
        self.operators = set(["+", "-", "*", "/", "**"])
        self.one_arg_functions = set(["n", "cos", "sin", "sqrt"]) # 'n' is unary negation
        self.two_arg_functions = set(["min", "max"])

    def evaluate_rpn_expression(self, tokens: Queue): # pylint: disable=too-many-statements
        """Evaluates an RPN/postfix expression (token by token) and returns the end result of the calculation.
        Uses an evaluation stack to handle the tokens. The last item left in the stack will be the end result.

        Args:
            tokens -- tokens that form an RPN/postfix mathematical expression
        
        Returns: The only object in the evaluation stack or error
        """
        evaluation_stack = Stack()

        if not tokens:
            raise InvalidExpressionException("No tokens to evaluate!")

        while not tokens.is_empty():
            token = tokens.dequeue()

            if isinstance(token, float):
                evaluation_stack.enqueue(token)
                continue

            if token in self.operators:
                if evaluation_stack.get_size() < 2:
                    raise InvalidExpressionException("Not enough operands for an operator")

                operand2 = evaluation_stack.dequeue()
                operand1 = evaluation_stack.dequeue()

                result = self._apply_operator(token, operand1, operand2)
                evaluation_stack.enqueue(result)

            elif token in self.one_arg_functions:
                if evaluation_stack.get_size() < 1:
                    raise InvalidExpressionException("Not enough operands for a one argument function")

                operand1 = evaluation_stack.dequeue()

                result = self._apply_one_arg_function(token, operand1)
                evaluation_stack.enqueue(result)

            elif token in self.two_arg_functions:
                if evaluation_stack.get_size() < 2:
                    raise InvalidExpressionException("Not enough operands for a one argument function")

                operand2 = evaluation_stack.dequeue()
                operand1 = evaluation_stack.dequeue()

                result = self._apply_two_arg_function(token, operand1, operand2)
                evaluation_stack.enqueue(result)

            else:
                raise InvalidExpressionException(f"Unrecognised token: {token}")

        if evaluation_stack.get_size() != 1:
            raise InvalidExpressionException("Too many items left in stack!")

        if evaluation_stack.peek().is_integer():
            return int(evaluation_stack.peek())
        return evaluation_stack.peek()

    def _apply_operator(self, operator: str, operand1: float, operand2: float):
        """Apply an operator on two operands (i.e. numbers).
        
        Args:
            operator -- the operator to be applied
            operand1 -- a number that the operator takes as first input
            operand2 -- a number that the operator takes as second input
        
        Returns: The result of the operation performed
        """
        try:
            match operator:
                case "+":
                    return operand1 + operand2
                case "-":
                    return operand1 - operand2
                case "*":
                    return operand1 * operand2
                case "/":
                    return operand1 / operand2
                case "**":
                    return operand1 ** operand2

        except OverflowError as e:
            raise InvalidExpressionException(
                "Maximum data limit exceeded! Please try a smaller calculation."
                ) from e
        except ZeroDivisionError as e:
            raise InvalidExpressionException("Division with zero undefined!") from e

    def _apply_one_arg_function(self, function: str, operand: float):
        """Apply a function on an argument/operand (i.e. number). In the cases of cos and sin
        the operand is first converted to radians.
        
        Args:
            function -- name of the function to be applied
            operand -- a number that the function takes as input
        
        Returns: The result of the operation performed
        """
        try:
            match function:
                case "n":
                    return -operand
                case "cos":
                    return math.cos(math.radians(operand))
                case "sin":
                    return math.sin(math.radians(operand))
                case "sqrt":
                    return math.sqrt(operand)
        except OverflowError as e:
            raise InvalidExpressionException(
                "Maximum data limit exceeded! Please try a smaller calculation."
                ) from e

    def _apply_two_arg_function(self, function: str, operand1: float, operand2: float):
        """Apply a function on two arguments/operands (i.e. numbers).
        
        Args:
            function -- name of the function to be applied
            operand1 -- a number that the function takes as first input
            operand2 -- a number that the function takes as second input
        
        Returns: The result of the operation performed
        """
        try:
            match function:
                case "min":
                    return min(operand1, operand2)
                case "max":
                    return max(operand1, operand2)
        except OverflowError as e:
            raise InvalidExpressionException(
                "Maximum data limit exceeded! Please try a smaller calculation."
                ) from e
