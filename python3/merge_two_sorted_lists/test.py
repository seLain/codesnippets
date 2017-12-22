import unittest
from main import Solution

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestSolutionMethods(unittest.TestCase):

	solution = Solution()
	def test_mergeTwoLists(self):
		# leetcode test 1
		l1 = ListNode(1)
		l1.next = ListNode(2)
		l1.next.next = ListNode(4)
		l2 = ListNode(1)
		l2.next = ListNode(3)
		l2.next.next = ListNode(4)
		l3 = self.solution.mergeTwoLists(l1, l2)
		self.assertEqual(l3, l1)
		while l3 != None:
			print(str(l3.val) + '-->')
			l3 = l3.next
		print("----------------------------")
		# leetcode test 2
		l1 = ListNode(2)
		l2 = ListNode(1)
		l3 = self.solution.mergeTwoLists(l1, l2)
		self.assertEqual(l3, l2)
		while l3 != None:
			print(str(l3.val) + '-->')
			l3 = l3.next

		# customized test

if __name__ == '__main__':
    unittest.main()