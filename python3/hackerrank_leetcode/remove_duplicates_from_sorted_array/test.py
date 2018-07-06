import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_longestCommonPrefix(self):
        # leetcode test
        self.assertEqual(self.solution.removeDuplicates([1,1,2]), 2)
        # customized test
        self.assertEqual(self.solution.removeDuplicates([]), 0)
        self.assertEqual(self.solution.removeDuplicates([1]), 1)
        self.assertEqual(self.solution.removeDuplicates([1,1,2,3,3]), 3)

if __name__ == '__main__':
    unittest.main()