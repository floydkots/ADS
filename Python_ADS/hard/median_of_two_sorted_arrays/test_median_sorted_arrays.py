from unittest import TestCase
# from .median_sorted_arrays import merge,find_median_sorted_arrays
from .median_sorted_arrays import find_median_sorted_arrays_recursive as find_median_sorted_arrays


# class TestMerge(TestCase):
#     def test_merges_non_repeating_unequal_length(self):
#         nums1 = [1, 3, 5]
#         nums2 = [2, 4]
#         expected = [1, 2, 3, 4, 5]
#         self.assertEqual(expected, merge(nums1, nums2))
#
#     def test_merges_repeating_unequal_length(self):
#         nums1 = [1, 3, 3]
#         nums2 = [2, 3]
#         expected = [1, 2, 3, 3, 3]
#         self.assertEqual(expected, merge(nums1, nums2))
#
#     def test_merges_non_repeating_equal_length(self):
#         nums1 = [2, 5, 6]
#         nums2 = [3, 4, 7]
#         expected = [2, 3, 4, 5, 6, 7]
#         self.assertEqual(expected, merge(nums1, nums2))
#
#     def test_merges_repeating_equal_length(self):
#         nums1 = [2, 2, 6]
#         nums2 = [3, 4, 4]
#         expected = [2, 2, 3, 4, 4, 6]
#         self.assertEqual(expected, merge(nums1, nums2))


class TestFindMedianSortedArrays(TestCase):
    def test_1_finds_median_of_odd_length(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(2.0, find_median_sorted_arrays(nums1, nums2))

    def test_2_finds_median_of_even_length(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(2.5, find_median_sorted_arrays(nums1, nums2))
