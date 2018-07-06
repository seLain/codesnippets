import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_checkPossibility(self):
        # leetcode test
        bool_isom = self.solution.checkPossibility([4,2,3])
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.checkPossibility([4,2,1])
        self.assertEqual(bool_isom, False)
        bool_isom = self.solution.checkPossibility([3,4,2,3])
        self.assertEqual(bool_isom, False)
        bool_isom = self.solution.checkPossibility([2,3,3,2,4])
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.checkPossibility([-1,4,2,3])
        self.assertEqual(bool_isom, True)
		
        # customized test
        bool_isom = self.solution.checkPossibility([1])
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.checkPossibility([2,1])
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.checkPossibility([4,4,3,4,4])
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.checkPossibility([4,4,4,4,2])
        self.assertEqual(bool_isom, True)

        import random
        data = [random.randint(-10, 10) for x in range(0, 100000)]
        bool_isom = self.solution.checkPossibility(data)
        self.assertEqual(bool_isom, False)
        
if __name__ == '__main__':
    unittest.main()