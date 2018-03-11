from unittest import TestCase
from .longest_substring import length_of_longest_substring


class TestLengthOfLongestSubstring(TestCase):
    def test_finds_abc_in_abcabcbb(self):
        self.assertEqual(3, length_of_longest_substring('abcabcbb'))

    def test_finds_b_from_bbbbb(self):
        self.assertEqual(1, length_of_longest_substring('bbbbb'))

    def test_finds_wke_in_pwwkew(self):
        self.assertEqual(3, length_of_longest_substring('pwwkew'))

    def test_finds_single_character_string(self):
        self.assertEqual(1, length_of_longest_substring('c'))

    def test_finds_ab_in_aab(self):
        self.assertEqual(2, length_of_longest_substring('aab'))

    def test_finds_vdf_in_dvdf(self):
        self.assertEqual(3, length_of_longest_substring('dvdf'))
