import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_generateParenthesis(self):
        # leetcode test
        result = self.solution.generateParenthesis(3)
        expect = ["((()))","(()())","(())()","()(())","()()()"]
        self.assertEqual(sorted(result), sorted(expect))
        # leetcode test 2
        result = self.solution.generateParenthesis(4)
        expect = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        self.assertEqual(sorted(result), sorted(expect))
        # customized test
        self.assertEqual(self.solution.generateParenthesis(0), [])

if __name__ == '__main__':
    unittest.main()