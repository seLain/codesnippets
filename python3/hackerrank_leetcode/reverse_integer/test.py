import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_reverse(self):
        # leetcode tests
        self.assertEqual(self.solution.reverse(123), 321)
        self.assertEqual(self.solution.reverse(-123), -321)
        self.assertEqual(self.solution.reverse(120), 21)
        # customized test
        self.assertEqual(self.solution.reverse(100), 1)
        self.assertEqual(self.solution.reverse(-0), 0)
        # boundary test
        self.assertEqual(self.solution.reverse(8463847412), 0)
        self.assertEqual(self.solution.reverse(-9463847412), 0)

if __name__ == '__main__':
    unittest.main()