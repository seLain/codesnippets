import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_convert(self):
        # leetcode test
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.solution.convert("ABCDE", 4), "ABCED")
        # customized test
        self.assertEqual(self.solution.convert("", 0), "")
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 0), "PAYPALISHIRING")
        self.assertEqual(self.solution.convert("PAYPALISHIRING", 1), "PAYPALISHIRING")
        self.assertEqual(self.solution.convert("P", 3), "P")

if __name__ == '__main__':
    unittest.main()