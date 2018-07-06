import unittest
from main import sockMerchant

class TestSolutionMethods(unittest.TestCase):

    def test_sockMerchant(self):
        # hackerrank tests
        n = 9 
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        expected = 3
        computed = sockMerchant(n, ar)
        self.assertEqual(expected, computed)

        # customized test
        n = 9
        ar = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        expected = 0
        computed = sockMerchant(n, ar)
        self.assertEqual(expected, computed)


if __name__ == '__main__':
    unittest.main()