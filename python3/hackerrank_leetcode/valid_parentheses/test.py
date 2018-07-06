import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_longestCommonPrefix(self):
        # leetcode test
        self.assertEqual(self.solution.isValid("()[]{}"), True)
        self.assertEqual(self.solution.isValid("()"), True)
        self.assertEqual(self.solution.isValid("(]"), False)
        self.assertEqual(self.solution.isValid("([)]"), False)
        self.assertEqual(self.solution.isValid("){"), False)
        self.assertEqual(self.solution.isValid("(("), False)
        # customized test
        self.assertEqual(self.solution.isValid("("), False)

if __name__ == '__main__':
    unittest.main()