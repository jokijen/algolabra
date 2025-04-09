"""
Performs the mathematical calculations for an expression in postfix notation. 
Returns the solution or an error message.
"""
import math
from .stack import Stack
from .queue import Queue
from .exceptions import InvalidExpressionException


class RPNEvaluator:
    def __init__(self):
        self.operators = set(["+", "-", "*", "/", "**"])
        self.one_arg_functions = set(["n", "cos", "sin", "sqrt"])
        self.two_arg_functions = set(["min", "max"])


    def evaluate_rpn_expression(self, tokens: Queue):
        evaluation_stack = Stack()

        if not tokens:
            raise InvalidExpressionException("No tokens to evaluate!")

        while not tokens.is_empty():
            token = tokens.dequeue()

            if isinstance(token, float):
                evaluation_stack.enqueue(token)
                continue

            elif token in self.one_arg_functions:
                if evaluation_stack.get_size() < 1:
                    raise InvalidExpressionException("Not enough operands for a one argument function")

                operand1 = evaluation_stack.dequeue()

                try:
                    result = self.apply_one_arg_function(token, operand1)
                    evaluation_stack.enqueue(result)
                except OverflowError as e:
                    raise InvalidExpressionException(
                        "Maximum data limit exceeded! Please try a smaller calculation."
                        )
    
            elif token in self.two_arg_functions:
                if evaluation_stack.get_size() < 2:
                    raise InvalidExpressionException("Not enough operands for a one argument function")
                operand2 = evaluation_stack.dequeue()
                operand1 = evaluation_stack.dequeue()

                try:
                    result = self.apply_two_arg_function(token, operand1, operand2)
                    evaluation_stack.enqueue(result)
                except OverflowError as e:
                    raise InvalidExpressionException(
                        "Maximum data limit exceeded! Please try a smaller calculation."
                        )

            elif token in self.operators:
                if evaluation_stack.get_size() < 2:
                    raise InvalidExpressionException("Not enough operands for a one argument function")
                operand2 = evaluation_stack.dequeue()
                operand1 = evaluation_stack.dequeue()

                try:
                    result = self.apply_operator(token, operand1, operand2)
                    evaluation_stack.enqueue(result)
                except OverflowError as e:
                    raise InvalidExpressionException(
                        "Maximum data limit exceeded! Please try a smaller calculation."
                        )
            else:
                raise InvalidExpressionException(f"Unrecognised token: {token}")

        if evaluation_stack.get_size() != 1:
            raise InvalidExpressionException("Something went wrong! :(")
        
        return evaluation_stack.peek()


    def apply_one_arg_function(self, function: str, operand: float):
        match function:
            case "n":
                return -operand
            case "cos":
                return math.cos(math.radians(operand))
            case "sin":
                return math.sin(math.radians(operand))
            case "sqrt":
                return math.sqrt(operand)

    def apply_two_arg_function(self, function: str, operand1: float, operand2: float):
        match function:
            case "min":
                return min(operand1, operand2)
            case "max":
                return max(operand1, operand2)

    def apply_operator(self, operator: str, operand1: float, operand2: float):
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
