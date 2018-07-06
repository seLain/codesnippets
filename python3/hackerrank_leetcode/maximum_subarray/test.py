import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_maxSubArray(self):
        # leetcode test
        data = [-2,1,-3,4,-1,2,1,-5,4]
        max_sum = self.solution.maxSubArray(data)
        self.assertEqual(max_sum, 6)
		
        # customized test
        data = []
        max_sum = self.solution.maxSubArray(data)
        self.assertEqual(max_sum, 0)

        data = [-1, 1]
        max_sum = self.solution.maxSubArray(data)
        self.assertEqual(max_sum, 1)

        data = [-1, -2]
        max_sum = self.solution.maxSubArray(data)
        self.assertEqual(max_sum, -1)
		
if __name__ == '__main__':
    unittest.main()