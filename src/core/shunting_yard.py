"""The Shunting-Yard algoritm used to convert an infix format mathematical expression given by the
user into RPN/postfix notation using a queue and a stack.
"""
from .stack import Stack
from .queue import Queue
from .exceptions import InvalidExpressionException


class ShuntingYard:
    """The class implements the Shunting-Yard algorithm that converts infix notation expressions into
    RPN/postfix by using a LIFO stack to hold operators and functions, and an output queue to hold
    the final output. Operators and functions are given a presedence, which (in addition to parentheses)
    ensure the correct order of operations.

    Attributes:
        operators (set): A set containing the allowed operators for the calculations
        functions (set): A set containing the allowed functions for the calculations
        precedence (dict): A dict containing the precedence of the operators and functions 

    Methods:
        convert_to_rpn(tokens): Converts a list of tokens that form an infix expression into RPN/postfix
    """
    def __init__(self):
        self.operators = set(["+", "-", "*", "/", "**"])
        # 'n' is the unary negation
        self.functions = set(["n", "cos", "sin", "sqrt", "min", "max"])
        self.precedence = {"+": 1,
                           "-": 1,
                           "max": 3,
                           "min": 3,
                           "n": 1,
                           "*": 2,
                           "/": 2,
                           "**": 3,
                           "sqrt": 3,
                           "cos": 4,
                           "sin": 4}

    def convert_to_rpn(self, tokens: list) -> Queue:  # pylint: disable=too-many-statements
        """Converts an infix mathematical expression to RPN/postfix.
        
        Args:
            tokens -- tokens that form an infix mathematical expression
        
        Returns: Queue object that contains the mathematical expression in PRN/postfix
        """
        operator_stack = Stack()
        output_queue = Queue()

        if not tokens:
            raise InvalidExpressionException("No tokens to evaluate!")

        while tokens:
            token = tokens.pop(0)

            if isinstance(token, float):
                output_queue.enqueue(token)
                continue

            if token == "(":
                operator_stack.enqueue(token)
                continue

            if token == ")":
                while not operator_stack.is_empty():
                    stack_top = operator_stack.dequeue()

                    if stack_top == "(":
                        break
                    output_queue.enqueue(stack_top)
                continue

            if token in self.operators or token in self.functions:
                while not operator_stack.is_empty():
                    prev_in_stack = operator_stack.peek()

                    if prev_in_stack == "(":
                        operator_stack.enqueue(token)
                        break

                    # Stack's top token has a lower precedence -> add token to stack
                    if self.precedence[token] > self.precedence[prev_in_stack]:
                        operator_stack.enqueue(token)
                        break

                    # Stack's top token has a higher or same precedence -> pop all the items with
                    # higher/same precedence and add them to the output queue
                    popped_token = operator_stack.dequeue()
                    output_queue.enqueue(popped_token)
                else:
                    operator_stack.enqueue(token)

        while not operator_stack.is_empty():
            popped_token = operator_stack.dequeue()
            output_queue.enqueue(popped_token)

        return output_queue
