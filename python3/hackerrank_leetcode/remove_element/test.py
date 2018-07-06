import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_longestCommonPrefix(self):
        # leetcode test
        self.assertEqual(self.solution.removeElement([3,2,2,3], 3), 2)
        # customized test
        self.assertEqual(self.solution.removeElement([], 3), 0)
        self.assertEqual(self.solution.removeElement([1], 3), 1)

if __name__ == '__main__':
    unittest.main()