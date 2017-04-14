import unittest
from algowk3 import find_sum
from hypothesis import given
import hypothesis.strategies as st

class MaxValContiguousSubsequenceTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(solve([]), None)

    def test_singleton_list(self):
        self.assertEqual(solve([1]), 1)
