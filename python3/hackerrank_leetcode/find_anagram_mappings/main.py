class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        if n == 0:
            return []
        elif n == 1:
            return [0]
        else:
            anagram_index = []
            for data in A:
                anagram_index.append(B.index(data))
            return anagram_index