import unittest
from coins import change



class ChangeMakingTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(change(0, []), 0)

    def test_single_amount(self):
        self.assertEqual(change(1, [1]), 1)

    def test_sample_list(self):
        self.assertEqual(change(4, [1, 2, 3]), 4)

    def test_big_list(self):
        self.assertEqual(change(5, [1, 2, 3]), 4)
