import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_divide(self):
        # leetcode test
        self.assertEqual(self.solution.divide(0, 1), 0)
        self.assertEqual(self.solution.divide(-1, 1), -1)
        self.assertEqual(self.solution.divide(-2147483648, -1), 2147483647)
        # customized test
        self.assertEqual(self.solution.divide(1, 0), None)
        self.assertEqual(self.solution.divide(4, 2), 2)
        self.assertEqual(self.solution.divide(4, 3), 1)
        self.assertEqual(self.solution.divide(1, -1), -1)
        self.assertEqual(self.solution.divide(-1, -1), 1)

if __name__ == '__main__':
    unittest.main()