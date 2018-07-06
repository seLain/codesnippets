import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_lastRemaining(self):
        # leetcode tests
        n = 9
        expected = 6
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)

        # customized test
        n = 1
        expected = 1
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)

        n = 2
        expected = 2
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)

        n = 3
        expected = 2
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)

        n = 21
        expected = 6
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)

        n = 22
        expected = 8
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)
        
        n = 10000000
        expected = 6150102
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)

        # this boundary test might crash your machine
        # please apply with caution
        '''
        n = 2147483648
        expected = 1431655766
        computed = self.solution.lastRemaining(n)
        self.assertEqual(expected, computed)
		'''

if __name__ == '__main__':
    unittest.main()