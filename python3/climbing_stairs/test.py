import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_climbStairs(self):
        # leetcode test
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)
        # customized test
        self.assertEqual(self.solution.climbStairs(0), 0)
        self.assertEqual(self.solution.climbStairs(1), 1)

if __name__ == '__main__':
    unittest.main()