from collections import deque

# A LIFO stack
class Stack:
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

    def is_empty(self):
        return len(self._tokens) == 0
    
    def get_size(self):
        return len(self._tokens)
