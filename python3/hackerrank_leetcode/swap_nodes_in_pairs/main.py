# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            # swap the first two
            first = head
            second = first.next
            first.next = second.next
            second.next = first
            # re-assign head
            head = second
            # move to next pair
            ordered_tail = first
            first = first.next
            # swap the rest
            while first is not None and first.next is not None:
                second = first.next
                first.next = second.next
                second.next = first
                ordered_tail.next = second
                ordered_tail = first
                first = first.next
            # iteration ends, return the new head
            return head