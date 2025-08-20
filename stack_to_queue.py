# [1, 2, 3, 4, 5]
# 1 = left most  use popleft() to remove top
# 5 = right most use pop()     to remove tail
# Append on top (left side) use appendleft()
# Append on tail (right side) use append()
import unittest
from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()
        # self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x) # Append on rightside
        for _ in range(len(self.q1) - 1):
            self.q1.append(self.q1.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        else:
            return False
        
class TestMyStack(unittest.TestCase):
    def test_empty_initially(self):
        s = MyStack()
        self.assertTrue(s.empty())

    def test_single_push_pop(self):
        s = MyStack()
        s.push(42)
        self.assertFalse(s.empty())
        self.assertEqual(s.top(), 42)
        self.assertEqual(s.pop(), 42)
        self.assertTrue(s.empty())

    def test_lifo_behavior(self):
        s = MyStack()
        s.push(1); s.push(2); s.push(3)
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.top(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertTrue(s.empty())

    def test_interleaved(self):
        s = MyStack()
        s.push(5)
        s.push(6)
        self.assertEqual(s.pop(), 6)
        s.push(7)
        self.assertEqual(s.top(), 7)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.pop(), 5)
        self.assertTrue(s.empty())

    def test_bulk(self):
        s = MyStack()
        for i in range(1000):
            s.push(i)
        for i in reversed(range(1000)):
            self.assertEqual(s.pop(), i)
        self.assertTrue(s.empty())

    def test_exceptions_on_empty(self):
        s = MyStack()
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.top()


if __name__ == "__main__":
    unittest.main()