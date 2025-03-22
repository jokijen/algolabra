from collections import deque

# A FIFO queue
class Queue:
    def __init__(self):
        self._tokens = deque()

    def enqueue(self, token):
        self._tokens.append(token)

    def dequeue(self):
        return self._tokens.popleft()
