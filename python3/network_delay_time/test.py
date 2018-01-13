import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_networkDelayTime(self):
        # leetcode tests

        # customized test
        times = [(1, 2, 1), (2, 1, 1)]
        N = 2
        K = 1
        expected = 1
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)

        times = [(1, 2, 1), (2, 1, 1), (3, 4, 1), (4, 3, 1)]
        N = 4
        K = 1
        expected = -1
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)

        times = [(1, 2, 1), (1, 3, 1), (3, 2, 1)]
        N = 3
        K = 1
        expected = 1
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)

        times = [(1, 2, 4), (3, 2, 2), (1, 3, 1)]
        N = 3
        K = 1
        expected = 3
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)

        times = [(1, 2, 1), (1, 3, 2), (3, 5, 1), (5, 4, 1), (2, 4, 7)]
        N = 5
        K = 1
        expected = 4
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)

        times = [(1, 2, 4), (1, 3, 1), (3, 2, 1), (2, 4, 1)]
        N = 4
        K = 1
        expected = 3
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)

        times = [[2,1,1],[2,3,1],[3,4,1]]
        N = 4
        K = 2
        expected = 2
        computed = self.solution.networkDelayTime(times, N, K)
        self.assertEqual(expected, computed)



if __name__ == '__main__':
    unittest.main()