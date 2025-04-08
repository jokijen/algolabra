"""Converts a user input into RPN/postfix notation using the Shunting-Yard algorithm. 
Returns the mathematical expression in RPN/postfix notation.
"""
from .stack import Stack
from .queue import Queue
from .exceptions import InvalidExpressionException


class ShuntingYard:
    """The class is used to convert the tokenised expression into RPN form
    """

    def __init__(self):
        self.operators = set(["+", "-", "n", "*", "/", "**"])
        self.functions = set(["cos", "sin", "sqrt", "min", "max"])
        # self.characters = set(["(", ")", "."])
        self.precedence = {"+": 1,
                           "-": 1,
                           "max": 1,
                           "min": 1,
                           "n": 1,
                           "*": 2,
                           "/": 2,
                           "**": 3,
                           "sqrt": 3,
                           "cos": 4,
                           "sin": 4}


    def convert_to_rpn(self, tokens):
        operator_stack = Stack()
        output_queue = Queue()

        while tokens:
            token = tokens.pop(0)

            if isinstance(token, float):
                output_queue.enqueue(token)
                continue

            if token == "(":
                operator_stack.enqueue(token)
                continue

            if token == ")":
                while operator_stack:
                    stack_top = operator_stack.dequeue()

                    if stack_top != "(":
                        break
                    output_queue.enqueue(stack_top)
                continue

            if token in self.operators or token in self.functions:
                while not operator_stack.is_empty():
                    prev_in_stack = operator_stack.peek()

                    # Stack is empty or has a lower precedence top token -> add token to stack
                    if prev_in_stack == None or self.precedence[token] > self.precedence[prev_in_stack]:
                        operator_stack.enqueue(token)
                        break

                    # Item on top of the stack has a higher precedence, you cannot add token to stack
                    # before popping off all the items with higher or same precedence
                    else:
                        popped_token = operator_stack.dequeue()
                        output_queue.enqueue(popped_token)
                else:
                    operator_stack.enqueue(token)

        while not operator_stack.is_empty():
            popped_token = operator_stack.dequeue()
            output_queue.enqueue(popped_token)

        return output_queue
