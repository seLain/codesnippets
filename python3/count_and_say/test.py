import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_countAndSay(self):
        # leetcode test
        self.assertEqual(self.solution.countAndSay(1), "1")
        self.assertEqual(self.solution.countAndSay(4), "1211")
        self.assertEqual(self.solution.countAndSay(10), "13211311123113112211")
        # customized test

if __name__ == '__main__':
    unittest.main()