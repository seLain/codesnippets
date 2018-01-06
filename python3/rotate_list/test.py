import unittest
from main import Solution

class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_rotateRight(self):
        # leetcode test 1
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        k = 2
        head = self.solution.rotateRight(head, k)
        self.assertEqual(head.val, 4)

        # leetcode test 2
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        k = 10
        head = self.solution.rotateRight(head, k)
        self.assertEqual(head.val, 3)
        
        # customized test
        head = ListNode(1)
        k = 2
        self.solution.rotateRight(head, k)
        self.assertEqual(head.val, 1)

        head = ListNode(1)
        head.next = ListNode(2)
        k = 2
        self.solution.rotateRight(head, k)
        self.assertEqual(head.val, 1)

if __name__ == '__main__':
    unittest.main()