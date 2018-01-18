from collections import defaultdict

class Solution:

    def remove_unique_chars(self, s, nonunique_chars):
        counter = 0
        list_s = list(s)
        while counter < len(list_s):
            if list_s[counter] not in nonunique_chars:
                del list_s[counter]
            else:
                counter += 1
        return ''.join(list_s)

    def commonChild(self, s1, s2):
        """
        :type s1, s2: str, str
        :rtype: int
        """
        # remove unique chars in both strs first
        s1 = self.remove_unique_chars(s1, set(s2))
        s2 = self.remove_unique_chars(s2, set(s1))

        if len(s1) == 0 or len(s2) == 0:
            return 0
        elif len(s1) == 1 and len(s2) == 1:
            return 1

        # LCS algo
        grid = []
        for i in range(0, len(s1)+1):
            grid.append([])
            for j in range(0, len(s2)+1):
                grid[i].append(0)

        for i in range(0, len(s1)):
            for j in range(0, len(s2)):
                if s1[i] == s2[j]:
                    grid[i+1][j+1] = grid[i][j] + 1
                else:
                    grid[i+1][j+1] = max(grid[i+1][j], grid[i][j+1])
        #print(grid)
        return grid[len(s1)][len(s2)]


