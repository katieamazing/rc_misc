import unittest
from remainder import chinese_remainder

class ChineseRemainderTheoremTests(unittest.TestCase):

    def test_empties(self):
        self.assertRaises(InputError, chinese_remainder, [], [])

    def test_pairs(self):
        self.assertRaises(InputError, chinese_remainder, [1,2], [5,7])

    def test_base(self):
        self.assertEqual(chinese_remainder([3,5,7], [2,3,2]), 23)

    def test_another(self):
        self.assertEqual(chinese_remainder([3,4,5], [2,3,1]), 11)
