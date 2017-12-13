class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # find shortest str first
        common_prefix = ""

        if len(strs) == 0:
            return common_prefix

        shortest_str = strs[0]
        for s in strs:
            if len(s) < len(shortest_str):
                shortest_str = s
        # judge by shortest_str, find the longest suspect first
        for i in range(len(shortest_str), 0, -1):
            suspect = shortest_str[0:i]
            counter = 0
            for s in strs:
                if s.startswith(suspect):
                    counter += 1
            if counter == len(strs):
                common_prefix = suspect
                break

        return common_prefix

