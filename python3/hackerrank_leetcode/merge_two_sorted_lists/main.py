# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
        	return l2
        elif l2 is None:
        	return l1

        if l1.val <= l2.val:
        	base_node = l1
        	l1 = l1.next
        else:
        	base_node = l2
        	l2 = l2.next

        new_l1 = l1
        new_l2 = l2
        new_base = base_node
        while new_l1 != None or new_l2 != None:
        	new_base, new_l1, new_l2 = self.__merge_front_nodes(new_base, new_l1, new_l2)

        return base_node

    def __merge_front_nodes(self, base_node, node1, node2):
    	
    	if node1 is None:
    		base_node.next = node2
    		return base_node.next, node1, node2.next

    	if node2 is None:
    		base_node.next = node1
    		return base_node.next, node1.next, node2

    	if node1.val < node2.val:
    		base_node.next = node1
    		return base_node.next, node1.next, node2
    	elif node1.val == node2.val:
    		new_node1 = node1.next
    		new_node2 = node2.next
    		base_node.next = node1
    		node1.next = node2
    		return node2, new_node1, new_node2
    	else:
    		base_node.next = node2
    		return base_node.next, node1, node2.next