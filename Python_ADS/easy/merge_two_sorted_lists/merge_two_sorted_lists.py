# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        while self and other:
            if self.val != other.val:
                return False
            else:
                self = self.next
                other = other.next
        return True

    def __str__(self):
        vals = []
        while self.next:
            vals += [self.val]
            self = self.next
        return str(vals + [self.val])


def merge_two_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    head = current = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    head = head.next
    return head


def merge_two_list_recursively(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = merge_two_list_recursively(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_list_recursively(l1, l2.next)
        return l2





