import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_isIsomorphic(self):
        # leetcode test
        bool_isom = self.solution.isIsomorphic("egg", "add")
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.isIsomorphic("foo", "bar")
        self.assertEqual(bool_isom, False)
        bool_isom = self.solution.isIsomorphic("paper", "title")
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.isIsomorphic("ab", "aa")
        self.assertEqual(bool_isom, False)
		
        # customized test
        bool_isom = self.solution.isIsomorphic("", "")
        self.assertEqual(bool_isom, True)
        bool_isom = self.solution.isIsomorphic("car", "mar")
        self.assertEqual(bool_isom, True)
        
if __name__ == '__main__':
    unittest.main()