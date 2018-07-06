import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_commonChild(self):
        
        # hackerrank test
        s1 = 'AA'
        s2 = 'BB'
        expected = 0
        result = self.solution.commonChild(s1, s2)
        self.assertEqual(result, expected)

        s1 = 'SHINCHAN'
        s2 = 'NOHARAAA'
        expected = 3
        result = self.solution.commonChild(s1, s2)
        self.assertEqual(result, expected)

        s1 = 'ABCDEF'
        s2 = 'FBDAMN'
        expected = 2
        result = self.solution.commonChild(s1, s2)
        self.assertEqual(result, expected)

        # customized test

        # time limitation test 1
        import random, copy, string
        s1 = ''.join([random.choice(string.ascii_uppercase) for x in range(0, 5000)])
        s2 = copy.copy(s1)
        expected = 5000
        result = self.solution.commonChild(s1, s2)
        self.assertEqual(result, expected)

        # time limitation test 2
        import random, copy, string
        s1 = ''.join([random.choice(string.ascii_uppercase) for x in range(0, 500)])
        s2 = ''.join([s1[i] for i in range(0, len(s1), 2)])
        expected = 250
        result = self.solution.commonChild(s1, s2)
        self.assertEqual(result, expected)

        # time limitation test 3
        # use with caution
        '''
        import random, copy, string
        s1 = ''.join([random.choice(string.ascii_uppercase) for x in range(0, 5000)])
        s2 = ''.join([random.choice(string.ascii_uppercase) for x in range(0, 4567)])
        expected = 235 # expected result varies acocording to random
        result = self.solution.commonChild(s1, s2)
        self.assertEqual(result, expected)
        '''

if __name__ == '__main__':
    unittest.main()