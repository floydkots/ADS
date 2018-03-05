from unittest import TestCase
from .add_two_numbers import add_two_numbers, ListNode


def create_list_from_digits(digits):
    first = current = ListNode(digits[0])
    for digit in digits[1:]:
        node = ListNode(digit)
        current.next = node
        current = current.next
    return first


class TestAddTwoNumbers(TestCase):
    def test_adds_given_sample(self):
        l1 = create_list_from_digits([2, 4, 3])
        l2 = create_list_from_digits([5, 6, 4])
        l3 = create_list_from_digits([7, 0, 8])

        self.assertEqual(str(l3), str(add_two_numbers(l1, l2)))

    def test_adds_single_digits(self):
        l1 = create_list_from_digits([9])
        l2 = create_list_from_digits([9])
        l3 = create_list_from_digits([8, 1])

        self.assertEqual(str(l3), str(add_two_numbers(l1, l2)))

    def test_adds_unequal_length_numbers(self):
        l1 = create_list_from_digits([1, 2, 3, 4])
        l2 = create_list_from_digits([3, 4])
        l3 = create_list_from_digits([4, 6, 3, 4])

        self.assertEqual(str(l3), str(add_two_numbers(l1, l2)))

    def test_can_carry_multiple_times(self):
        l1 = create_list_from_digits([7, 8, 9])
        l2 = create_list_from_digits([9, 9, 9])
        l3 = create_list_from_digits([6, 8, 9, 1])

        self.assertEqual(str(l3), str(add_two_numbers(l1, l2)))

