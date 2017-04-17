import unittest
from algowk2 import binarysearch, mergesort, guts
from hypothesis import given
import hypothesis.strategies as st


    #method format
    #def test_description(self):
        #self.assertTypeofAssert(testedfunction(testarg), expectedreturn)

#@given(st.lists(st.integers()))


class BinarySearchTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(binarysearch([], 1))

    def test_list_of_one_not(self):
        self.assertFalse(binarysearch([2], 1))

    def test_list_of_one_in(self):
        self.assertEqual(binarysearch([1], 1), 0)

    def test_a_big_list(self):
        self.assertEqual(binarysearch([1, 3, 4, 5, 6, 8], 5), 3)

    def test_a_big_odd_list(self):
        self.assertEqual(binarysearch([3, 6, 7, 8, 9], 7), 2)


class MergeSortTests(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mergesort([]), [])

    def test_list_of_one(self):
        self.assertEqual(mergesort([1]), [1])

    @given(st.lists(st.integers()))
    def test_a_harder_one(self, the_list):
        self.assertEqual(mergesort(the_list), sorted(the_list))

class GutsTests(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(guts([], []), [])

    def test_one_list_has_an_item(self):
        self.assertEqual(guts([1], []), [1])

    def test_single_item_lists(self):
        self.assertEqual(guts([2], [1]), [1, 2])

    def test_a_real_list_now(self):
        self.assertEqual(guts([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
