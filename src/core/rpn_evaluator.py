"""The PRN evaluator used for evaluating a RPN/postfix notation mathematical expression.
"""
import math
from .stack import Stack
from .queue import Queue
from .exceptions import InvalidExpressionException


class RPNEvaluator:
    """The class implements an evaluator for an RPN/postfix mathematical expression and returns
    the final result of the calculation. 

    Tokens from the input token queue are taken one at a time, from left to right. If the token is
    a number, it is placed in the evaluation stack (LIFO-structure). If the token is an operator or
    function, the required number of operands are popped from the evaluation stack and the calculation
    is performed. The result of this is then placed into the evaluation stack. Once all the input
    tokens have been processed, there should only be one number left in the evaluation stack: the
    final result.

    An error is raised if there is and unrecognised token, there are insufficient operands, or the
    calculation includes division with zero, taking a square root of a negative nmuber, or an overly
    large calculation.

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
        self.one_operand_operations = set(["n", "cos", "sin", "sqrt"])  # 'n' is unary negation
        self.two_operand_operations = set(["+", "-", "*", "/", "**", "min", "max"])

    def evaluate_rpn_expression(self, tokens: Queue):  # pylint: disable=too-many-statements
        """Evaluates an RPN/postfix expression (token by token) and returns the end result of the calculation.
        Uses an evaluation stack to handle the tokens. The last item left in the stack will be the end result.

        Args:
            tokens -- tokens that form an RPN/postfix mathematical expression

        Returns: The only object in the evaluation stack or error
        """
        evaluation_stack = Stack()

        if tokens.is_empty():
            raise InvalidExpressionException("No tokens to evaluate!")

        while not tokens.is_empty():
            token = tokens.dequeue()

            if isinstance(token, float):
                evaluation_stack.enqueue(token)
                continue

            if token in self.one_operand_operations:
                if evaluation_stack.get_size() < 1:
                    raise InvalidExpressionException("Not enough operands, one required")

                operand = evaluation_stack.dequeue()

                result = self._apply_operation(token, None, operand)
                evaluation_stack.enqueue(result)

            elif token in self.two_operand_operations:
                if evaluation_stack.get_size() < 2:
                    raise InvalidExpressionException("Not enough operands, two required")

                operand2 = evaluation_stack.dequeue()
                operand1 = evaluation_stack.dequeue()

                result = self._apply_operation(token, operand1, operand2)
                evaluation_stack.enqueue(result)

            else:
                raise InvalidExpressionException(f"Unrecognised token: {token}")

        if evaluation_stack.get_size() != 1:
            raise InvalidExpressionException("Too many items left in stack!")

        if evaluation_stack.peek().is_integer():
            return int(evaluation_stack.peek())
        return round(evaluation_stack.peek(), 10)

    def _apply_operation(self, function: str, operand1: float, operand2: float):  # pylint: disable=too-many-return-statements
        """Apply a function or operator on two operands (i.e. numbers).

        Args:
            function -- name of the function (may be an operator) to be applied
            operand1 -- a number that the operator takes as first input
            operand2 -- a number that the operator takes as second input

        Returns: The result of the operation performed
        """
        try:
            match function:
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
                case "sqrt":
                    try:
                        return math.sqrt(operand2)
                    except ValueError as e:
                        raise InvalidExpressionException(
                            "sqrt(x) is defined for positive input only!") from e
                case "n":
                    return -operand2
                case "cos":
                    return math.cos(math.radians(operand2))
                case "sin":
                    return math.sin(math.radians(operand2))
                case "min":
                    return min(operand1, operand2)
                case "max":
                    return max(operand1, operand2)

        except OverflowError as e:
            raise InvalidExpressionException(
                "Maximum data limit exceeded! Please try a smaller calculation."
            ) from e
        except ZeroDivisionError as e:
            raise InvalidExpressionException("Division with zero undefined!") from e
