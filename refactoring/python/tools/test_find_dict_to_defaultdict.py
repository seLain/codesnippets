import unittest
from find_dict_to_defaultdict import find_dict_to_defaultdict

class TestSolutionMethods(unittest.TestCase):

    def test_find_dict_to_defaultdict(self):
        
        results = find_dict_to_defaultdict('test_data')
        expected = {'test_data\\main.py': [3], 
                    'test_data\\sub_folder\\main.py': [3]}
        self.assertEqual(results, expected)
        
if __name__ == '__main__':
    unittest.main()