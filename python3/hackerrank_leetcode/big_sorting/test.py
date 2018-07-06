import unittest
from main import bigSorting
from random import randint
import copy 

class TestSolutionMethods(unittest.TestCase):

    def bigIntStrGenerator(self, n_digits):
        return ''.join([str(randint(1, 9))]+\
                       [str(randint(0, 9)) for x in range(n_digits-1)])

    def test_bigSorting(self):

        # hackerrank test

        arr = ['31415926535897932384626433832795', '1', '3', '10', '3', '5']
        expected = ['1', '3', '3', '5', '10', '31415926535897932384626433832795']
        sorted_arr = bigSorting(arr)
        self.assertEqual(expected, sorted_arr)

        # customized test

        arr = []
        expected = []
        sorted_arr = bigSorting(arr)
        self.assertEqual(expected, sorted_arr)

        arr = ['1']
        expected = ['1']
        sorted_arr = bigSorting(arr)
        self.assertEqual(expected, sorted_arr)

        # time limitation test
        # this might hang your machine please use with caution
        expected = [self.bigIntStrGenerator(x) for x in range(pow(10, 0), pow(10, 4))]
        arr = copy.copy(expected)
        for i in range(0, 1000):
            idx1 = randint(1, len(arr)-1)
            idx2 = randint(1, len(arr)-1)
            arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        sorted_arr = bigSorting(arr)
        self.assertEqual(expected, sorted_arr)

if __name__ == '__main__':
    unittest.main()