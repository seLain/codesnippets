import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_rotate(self):
        # leetcode test 1
        '''
        list1 = [[1,2,3],[4,5,6],[7,8,9]]
        list2 = [[7,4,1],[8,5,2],[9,6,3]]
        self.solution.rotate(list1)
        self.assertEqual(list1, list2)
        '''
        
        list1 = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
        list2 = [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]]
        self.solution.rotate(list1)
        self.assertEqual(list1, list2)
        
        # customized test
        list1 = []
        list2 = []
        self.solution.rotate(list1)
        self.assertEqual(list1, list2)

if __name__ == '__main__':
    unittest.main()