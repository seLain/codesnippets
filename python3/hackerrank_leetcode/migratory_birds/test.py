import unittest
from main import migratoryBirds

class TestSolutionMethods(unittest.TestCase):

    def test_migratoryBirds(self):
        # hackerrank tests
        n = 6 
        ar = [1, 4, 4, 4, 5, 3]
        expected = 4
        computed = migratoryBirds(n, ar)
        self.assertEqual(expected, computed)

        # customized test
        n = 6 
        ar = [1, 4, 4, 2, 3, 3]
        expected = 3
        computed = migratoryBirds(n, ar)
        self.assertEqual(expected, computed)


if __name__ == '__main__':
    unittest.main()