import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_asteroidCollision(self):
        # leetcode tests
        asteroids = [5, 10, -5]
        expected = [5, 10]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [8, -8]
        expected = []
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [10, 2, -5]
        expected = [10]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [-2, -1, 1, 2]
        expected = [-2, -1, 1, 2]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [1, 1, -1, -1]
        expected = []
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        # customized test
        asteroids = []
        expected = []
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [1, -1, -1, 1]
        expected = [-1, 1]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [-1, 1, 1, -1]
        expected = [-1, 1]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [1, -1, 1, -1]
        expected = []
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        asteroids = [1, 1, -1, -1, -1]
        expected = [-1]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        import random
        asteroids = []
        for i in range(0, 10000):
            if i%2 == 0:
                asteroids.append(1)
            else:
                asteroids.append(-1)
        expected = []
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)

        # worst case test
        asteroids = [1 for x in range(0, 9999)]
        asteroids.append(-2)
        expected = [-2]
        computed = self.solution.asteroidCollision(asteroids)
        self.assertEqual(expected, computed)


if __name__ == '__main__':
    unittest.main()