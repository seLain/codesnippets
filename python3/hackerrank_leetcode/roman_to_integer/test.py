import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_romanToInt(self):
        # leetcode test
        self.assertEqual(self.solution.romanToInt("DCXXI"), 621)
        # customized test
        self.assertEqual(self.solution.romanToInt("CXCIX"), 199)
        # boundary test
        self.assertEqual(self.solution.romanToInt("I"), 1)
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)

if __name__ == '__main__':
    unittest.main()