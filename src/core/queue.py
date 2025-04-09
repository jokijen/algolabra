from collections import deque

# A FIFO queue
class Queue:
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
