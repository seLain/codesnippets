import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_isHappy(self):
        # leetcode test
        bool_result = self.solution.isHappy(19)
        self.assertEqual(bool_result, True)
        
        # customized test
        bool_result = self.solution.isHappy(-1)
        self.assertEqual(bool_result, False)
        bool_result = self.solution.isHappy(0)
        self.assertEqual(bool_result, False)
        bool_result = self.solution.isHappy(1)
        self.assertEqual(bool_result, True)
        bool_result = self.solution.isHappy(7)
        self.assertEqual(bool_result, True)
        bool_result = self.solution.isHappy(9)
        self.assertEqual(bool_result, False)
        bool_result = self.solution.isHappy(10)
        self.assertEqual(bool_result, True)
        # boundary test
        bool_result = self.solution.isHappy(2147483647)
        self.assertEqual(bool_result, False)
        
		
if __name__ == '__main__':
    unittest.main()