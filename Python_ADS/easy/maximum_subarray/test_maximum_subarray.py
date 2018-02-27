from unittest import TestCase
from .maximum_subarray import maximum_sub_array


class TestMaximumSubarray(TestCase):
    def test_0_correctly_finds_max_sum(self):
        self.assertEqual(21, maximum_sub_array([2, 3, 4, 5, 7]))

    def test_1_correctly_finds_max_sum(self):
        self.assertEqual(6, maximum_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

    def test_2_correctly_finds_max_sum(self):
        self.assertEqual(7, maximum_sub_array([-2, 1, -5, 4, -1, 2, 1, -3, 4]))
