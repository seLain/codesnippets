# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        elif head.next is None:
            return True
        else:
            left_head = None
            forward_flag = head
            forward_counter = 0
            while forward_flag is not None:
                forward_flag = forward_flag.next
                forward_counter += 1
                if forward_counter%2 == 0:
                    # move and reverse
                    temp = left_head
                    left_head = head
                    head = head.next
                    left_head.next = temp

            # determine if left_head is at center node
            if forward_counter%2 == 0:
                right_head = head
            else:
                right_head = head.next

            # start to check
            while left_head != None and right_head != None:
                if left_head.val != right_head.val:
                    return False
                else:
                    left_head = left_head.next
                    right_head = right_head.next

            # if successfully runs to both ends
            return True
