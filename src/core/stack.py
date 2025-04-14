from collections import deque


class Stack:
    """A last-in-first-out (LIFO) stack that can be used when implementing the Shunting-Yard algorithm.

    Attributes:
        _tokens (deque): A deque ("double-ended-queue") used to hold tokens

    Methods:
        enqueue(token): Adds the token to the (top of) the stack
        dequeue: Removes and returns the token from top of the stack
        peek: Returns the token on top of the stack, but does not remove it from the stack
        is_empty: Returns True if the stack has no items, False if it does
        get_size: Returns the number of items in the stack
    """
    def __init__(self):
        self._tokens = deque()

    def enqueue(self, token):
        self._tokens.append(token)

    def dequeue(self):
        return self._tokens.pop()

    def peek(self):
        if self._tokens:
            return self._tokens[-1]
        return None

    def is_empty(self) -> bool:
        return len(self._tokens) == 0

    def get_size(self) -> int:
        return len(self._tokens)
