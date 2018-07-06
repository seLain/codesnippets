import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_dominantIndex(self):
        # leetcode tests
        nums = [3, 6, 1, 0]
        expected = 1
        computed = self.solution.dominantIndex(nums)
        self.assertEqual(expected, computed)

        nums = [1, 2, 3, 4]
        expected = -1
        computed = self.solution.dominantIndex(nums)
        self.assertEqual(expected, computed)

        nums = [1,0]
        expected = 0
        computed = self.solution.dominantIndex(nums)
        self.assertEqual(expected, computed)

        # customized test
        nums = [1]
        expected = 0
        computed = self.solution.dominantIndex(nums)
        self.assertEqual(expected, computed)

if __name__ == '__main__':
    unittest.main()