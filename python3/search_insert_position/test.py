import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_searchInsert(self):
        # leetcode test
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 5), 2)
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 7), 4)
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 0), 0)
        self.assertEqual(self.solution.searchInsert([1], 0), 0)
        # customized test
        self.assertEqual(self.solution.searchInsert([], 0), 0)
        
if __name__ == '__main__':
    unittest.main()