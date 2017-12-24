import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_lengthOfLastWord(self):
        # leetcode test
        self.assertEqual(self.solution.lengthOfLastWord("Hello World"), 5)
        self.assertEqual(self.solution.lengthOfLastWord(""), 0)
        self.assertEqual(self.solution.lengthOfLastWord("Hello "), 5)
        self.assertEqual(self.solution.lengthOfLastWord("Hello"), 5)
        # customized test

if __name__ == '__main__':
    unittest.main()