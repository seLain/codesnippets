import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_longestCommonPrefix(self):
        # leetcode test
        self.assertEqual(self.solution.longestCommonPrefix([]), "")
        # customized test
        self.assertEqual(self.solution.longestCommonPrefix(["b", "c", "abc"]), "")
        self.assertEqual(self.solution.longestCommonPrefix(["ac", "ab", "abc"]), "a")
        self.assertEqual(self.solution.longestCommonPrefix(["abc", "abc"]), "abc")

if __name__ == '__main__':
    unittest.main()