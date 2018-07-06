import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_anagramMappings(self):
        # leetcode tests
        data_1 = [12, 28, 46, 32, 50]
        data_2 = [50, 12, 32, 46, 28]
        expected = [1, 4, 3, 2, 0]
        computed = self.solution.anagramMappings(data_1, data_2)
        self.assertEqual(expected, computed)

        # customized test
        data_1 = []
        data_2 = []
        expected = []
        computed = self.solution.anagramMappings(data_1, data_2)
        self.assertEqual(expected, computed)

        import random
        data_1 = [random.randint(0, pow(10,5)-1) for x in range(1, 101)]
        data_2 = [None for x in range(1, 101)]
        expected = []
        index = 0
        while index < 100:
            mapped_index = random.randint(0, 99)
            if data_2[mapped_index] is None:
                data_2[mapped_index] = data_1[index]
                expected.append(mapped_index)
                index += 1
        computed = self.solution.anagramMappings(data_1, data_2)
        self.assertEqual(expected, computed)
        

if __name__ == '__main__':
    unittest.main()