from unittest import TestCase
from .two_sum import twoSum


class TestTwoSum(TestCase):
    def test_with_1_item_array(self):
        self.assertEqual(False, twoSum([1], 1),
                         "twoSum should return False if the length of the submitted array is less or equal to 1")

    def test_with_4_item_array(self):
        self.assertEqual([0, 1], twoSum([2, 7, 11, 15], 9))

    def test_with_no_two_sum(self):
        self.assertEqual(None, twoSum([2, 7, 11, 15], 30))
