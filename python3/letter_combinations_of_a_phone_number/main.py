class Solution:

    mapping = {'2': ['a', 'b', 'c'], 
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z'],}

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return self.mapping[digits]
        else:
            cur_digit = digits[0]
            sub_digits = digits[1:]
            sub_combs = self.letterCombinations(sub_digits)
            return_combs = []
            for comb in sub_combs:
                for head_letter in self.mapping[cur_digit]:
                    return_combs.append(head_letter+comb)
            return return_combs

