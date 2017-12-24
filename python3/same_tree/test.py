import unittest
from main import Solution

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_isSameTree(self):
        # leetcode test 1
        root1= TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)
        root2= TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertEqual(self.solution.isSameTree(root1, root2), True)
        # leetcode test 2
        root1= TreeNode(1)
        root1.left = TreeNode(2)
        root2= TreeNode(1)
        root2.right = TreeNode(2)
        self.assertEqual(self.solution.isSameTree(root1, root2), False)
        # leetcode test 3
        root1= TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(1)
        root2= TreeNode(1)
        root2.left = TreeNode(1)
        root2.right = TreeNode(2)
        self.assertEqual(self.solution.isSameTree(root1, root2), False)
        # customized test

if __name__ == '__main__':
    unittest.main()