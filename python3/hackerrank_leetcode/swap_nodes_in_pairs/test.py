import unittest
from main import Solution

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_swapPairs(self):
        # leetcode test
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        newhead = self.solution.swapPairs(head)
        self.assertEqual(newhead.val, 2)
        self.assertEqual(newhead.next.val, 1)
        self.assertEqual(newhead.next.next.val, 4)
        self.assertEqual(newhead.next.next.next.val, 3)
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        newhead = self.solution.swapPairs(head)
        self.assertEqual(newhead.val, 2)
        self.assertEqual(newhead.next.val, 1)
        self.assertEqual(newhead.next.next.val, 3)
        # customized test
        newhead = self.solution.swapPairs(None)
        self.assertEqual(newhead, None)
        head = ListNode(1)
        newhead = self.solution.swapPairs(head)
        self.assertEqual(newhead.val, 1)
        head = ListNode(1)
        head.next = ListNode(2)
        newhead = self.solution.swapPairs(head)
        self.assertEqual(newhead.val, 2)
        self.assertEqual(newhead.next.val, 1)
        self.assertEqual(newhead.next.next, None)
        

if __name__ == '__main__':
    unittest.main()