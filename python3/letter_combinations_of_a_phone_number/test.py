import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_letterCombinations(self):
        # leetcode test 1
        result = self.solution.letterCombinations("23")
        expect = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(result), sorted(expect))
        # leetcode test 2
        result = self.solution.letterCombinations("")
        self.assertEqual(result, [])
        # customized test
        
if __name__ == '__main__':
    unittest.main()