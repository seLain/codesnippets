# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return None

        base_flag = head
        forward_flag = base_flag.next
        while forward_flag != None:
        	if forward_flag.val == base_flag.val:
        		forward_flag = forward_flag.next
        		base_flag.next = forward_flag
        	else:
        		base_flag = forward_flag
        		forward_flag = forward_flag.next

        return head
