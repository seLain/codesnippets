# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)  # empty lead node of return list
        r = head # moving flag
        get_val = lambda x: 0 if x == None else x.val
        carry = 0
        while l1 != None or l2 != None:
            l1_val = get_val(l1)
            l2_val = get_val(l2)
            temp_sum = l1_val + l2_val + carry
            if temp_sum >= 10:
                carry = 1
                remainder = temp_sum - 10
            else:
                carry = 0
                remainder = temp_sum
            r.next = ListNode(remainder)
            # move to next digit
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            r = r.next
        # deal with last digit
        if carry != 0:
            r.next = ListNode(carry)

        return head.next