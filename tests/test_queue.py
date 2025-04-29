import unittest
from src.core.queue import Queue


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(repr(self.queue), "[1, 2, 3]")

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        token = self.queue.dequeue()
        self.assertEqual(token, 1)
        self.assertEqual(repr(self.queue), "[2, 3]")

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
