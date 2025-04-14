from collections import deque


class Queue:
    """A first-in-first-out (FIFO) queue that can be used when implementing the Shunting-Yard algorithm.

    Attributes:
        _tokens (deque): A deque ("double-ended-queue") used to hold tokens

    Methods:
        __repr__: Returns the tokens as a list
        enqueue(token): Adds the token to the end of the queue
        dequeue: Removes and returns the token at the start (left) of the queue
        is_empty: Returns True if the queue has no items, False if it does
    """
    def __init__(self):
        self._tokens = deque()

    def __repr__(self):
        return repr(list(self._tokens))

    def enqueue(self, token):
        self._tokens.append(token)

    def dequeue(self):
        return self._tokens.popleft()

    def is_empty(self):
        return len(self._tokens) == 0
