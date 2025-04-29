import unittest
from src.core.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_enqueue(self):
        self.stack.enqueue(1)
        self.stack.enqueue(2)
        self.stack.enqueue(3)
        self.assertEqual(len(self.stack._tokens), 3)

    def test_dequeue(self):
        self.stack.enqueue(1)
        self.stack.enqueue(2)
        self.stack.enqueue(3)
        token = self.stack.dequeue()
        self.assertEqual(token, 3)
        self.assertEqual(len(self.stack._tokens), 2)

    def test_peek_non_empty_stack(self):
        self.stack.enqueue(1)
        self.stack.enqueue(2)
        self.stack.enqueue(3)
        token = self.stack.peek()
        self.assertEqual(token, 3)
        self.assertEqual(len(self.stack._tokens), 3)

    def test_peek_empty_stack(self):
        self.assertIsNone(self.stack.peek())

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.enqueue(1)
        self.assertFalse(self.stack.is_empty())
