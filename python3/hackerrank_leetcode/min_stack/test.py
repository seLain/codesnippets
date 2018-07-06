import unittest
from main import MinStack

class TestSolutionMethods(unittest.TestCase):

    minStack = MinStack()

    def test_searchInsert(self):
        # leetcode test
        self.minStack.push(-2);
        self.minStack.push(0);
        self.minStack.push(-3);
        self.assertEqual(self.minStack.getMin(), -3)
        self.minStack.pop();
        self.assertEqual(self.minStack.top(), 0)
        self.assertEqual(self.minStack.getMin(), -2)
        # customized test
        
        
if __name__ == '__main__':
    unittest.main()