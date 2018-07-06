import unittest
from main import Solution

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_isPalindrome(self):

        # customized test

        self.assertEqual(self.solution.isPalindrome(None), True)

        head = ListNode('a')
        self.assertEqual(self.solution.isPalindrome(head), True)

        head = ListNode('a')
        head.next = ListNode('a')
        self.assertEqual(self.solution.isPalindrome(head), True)

        head = ListNode('a')
        head.next = ListNode('b')
        self.assertEqual(self.solution.isPalindrome(head), False)
        

if __name__ == '__main__':
    unittest.main()