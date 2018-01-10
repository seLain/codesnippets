import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_findRestaurant(self):
        # leetcode tests
        data_1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        data_2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        expected = ["Shogun"]
        computed = self.solution.findRestaurant(data_1, data_2)
        self.assertEqual(expected.sort(), computed.sort())

        data_1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        data_2 = ["KFC", "Shogun", "Burger King"]
        expected = ["Shogun"]
        computed = self.solution.findRestaurant(data_1, data_2)
        self.assertEqual(expected.sort(), computed.sort())
        # customized test
        data_1 = []
        data_2 = []
        expected = []
        computed = self.solution.findRestaurant(data_1, data_2)
        self.assertEqual(expected.sort(), computed.sort())

        data_1 = ["Shogun", "KFC", "Tapioca Express", "Burger King"]
        data_2 = ["KFC", "Shogun", "Burger King"]
        expected = ["Shogun", "KFC"]
        computed = self.solution.findRestaurant(data_1, data_2)
        self.assertEqual(expected.sort(), computed.sort())

        data_1 = [str(x) for x in range(1, 50000)]
        data_2 = [str(x) for x in range(1, 50000)]
        expected = [str(x) for x in range(1, 50000)]
        computed = self.solution.findRestaurant(data_1, data_2)
        self.assertEqual(expected.sort(), computed.sort())

if __name__ == '__main__':
    unittest.main()