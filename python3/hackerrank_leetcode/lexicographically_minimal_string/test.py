import unittest
from main import Solution

class TestSolutionMethods(unittest.TestCase):

    solution = Solution()

    def test_lexicographically_minimal_string(self):
    	# test in hackerrank discussion
        a = "ABA"
        b = "ABAA"
        expected = "AABAABA"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "ZZYYZZZA"
        b = "ZZYYZZZB"
        expected = "ZZYYZZYYZZZAZZZB"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "DAD"
        b = "DABC"
        expected = "DABCDAD"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "ABCBA"
        b = "BCBA"
        expected = "ABBCBACBA"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)
        
        # hackerrank test
        
        a = "JACK"
        b = "DANIEL"
        expected = "DAJACKNIEL"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "ABACABA"
        b = "ABACABA"
        expected = "AABABACABACABA"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        # customized test
        
        a = "BA"
        b = "BC"
        expected = "BABC"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "BBA"
        b = "BBC"
        expected = "BBABBC"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "BABC"
        b = "BBAC"
        expected = "BABBABCC"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        a = "BBBA"
        b = "BBC"
        expected = "BBBABBC"
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)

        
        # time limitation test
        a = ['B'] * 9999 + ['A']
        a = ''.join(a)
        b = ['B'] * 9999 + ['C']
        b = ''.join(b)
        expected = ''.join([a, b])
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)
        
        # time limitation boundary test
        # use with caution
        a = ["B"] * 99999 + ['A']
        a = ''.join(a)
        b = ["B"] * 99999 + ['C']
        b = ''.join(b)
        expected = ''.join([a, b])
        result = self.solution.lexicographically_minimal_string(a, b)
        self.assertEqual(result, expected)
        

if __name__ == '__main__':
    unittest.main()