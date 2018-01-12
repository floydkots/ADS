from unittest import TestCase
from .count_and_say import count_and_say


class TestCountAndSay(TestCase):
    def test_0_returns_empty_string_for_zeroth(self):
        self.assertEqual('', count_and_say(0))

    def test_1_returns_1_for_1(self):
        self.assertEqual('1', count_and_say(1))

    def test_2_returns_11_for_2(self):
        self.assertEqual('11', count_and_say(2))

    def test_3_returns_21_for_3(self):
        self.assertEqual('21', count_and_say(3))

    def test_4_returns_correct_for_6(self):
        self.assertEqual('312211', count_and_say(6))