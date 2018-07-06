import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_isPalindrome(self):
        # customized test
        self.assertEqual(self.solution.isPalindrome(1221), True)
        self.assertEqual(self.solution.isPalindrome(-1221), False)
        # boundary test
        self.assertEqual(self.solution.isPalindrome(2147483647), False)
        self.assertEqual(self.solution.isPalindrome(2147447412), True)
        self.assertEqual(self.solution.isPalindrome(2147557412), False)
        self.assertEqual(self.solution.isPalindrome(-2147483648), False)
        self.assertEqual(self.solution.isPalindrome(-2147447412), False)
        self.assertEqual(self.solution.isPalindrome(-2147557412), False)

if __name__ == '__main__':
    unittest.main()