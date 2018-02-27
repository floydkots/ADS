from unittest import TestCase
from .plus_one import plus_one


class TestPlusOne(TestCase):
    def test_adds_1_to_0(self):
        self.assertEqual([1], plus_one([0]))

    def test_adds_1_to_9(self):
        self.assertEqual([1, 0], plus_one([9]))

    def test_adds_1_to_10(self):
        self.assertEqual([1, 1], plus_one([1, 0]))

    def test_adds_1_to_101(self):
        self.assertEqual([1, 0, 2], plus_one([1, 0, 1]))
