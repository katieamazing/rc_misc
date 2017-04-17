import unittest
from algowk3 import solve
from hypothesis import given
import hypothesis.strategies as st



class MaxValContiguousSubsequenceTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(solve([]), 0)

    def test_singleton_list(self):
        self.assertEqual(solve([1]), 1)

    def test_jn_list(self):
        self.assertEqual(solve([1, -1, 2, -3, 5, 8]), 13)
