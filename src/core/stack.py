from collections import deque

# A LIFO stack
class Stack:
    def __init__(self):
        self._tokens = deque()

    def enqueue(self, token):
        self._tokens.append(token)

    def dequeue(self):
        return self._tokens.pop()
