class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < 2:
            return True
        else:
            return self.one_way_isIsomorphic(s, t) and \
                    self.one_way_isIsomorphic(t, s)

    def one_way_isIsomorphic(self, s, t):
        char_map = {}  # {replaced: mapped, }
        for i in range(0, len(s)):
            replaced = s[i]
            mapped = t[i]
            if replaced not in char_map.keys():
                char_map[replaced] = mapped
            else:
                if mapped != char_map[replaced]:
                    return False
        return True

        





