# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        n = 0
        node = head
        while node is not None:
            n += 1
            if node.next is None:
                node.next = head
                break
            else:
                node = node.next

        effective_rotates = k if k < n else k%n
        head_shift = n - effective_rotates

        for i in range(0, head_shift-1):
            head = head.next

        temp = head.next
        head.next = None
        head = temp

        return head