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

    def directed_commonChild(self, s1, s2):

        common_count = 0
        flag_s1 = 0
        flag_s2 = 0
        for i in range(0, len(s1)):
            flag_s1 = i
            flag_s2 = 0
            temp_count = 0
            while flag_s1 < len(s1) - common_count:
                if flag_s2 < len(s2):
                    for j in range(flag_s2, len(s2)):
                        if s1[flag_s1] == s2[j]:
                            temp_count += 1
                            flag_s1 += 1
                            flag_s2 = j + 1
                        if flag_s1 == len(s1):
                            break
                flag_s1 += 1
            if temp_count > common_count:
                common_count = temp_count

        return common_count

    def commonChild(self, s1, s2):
        """
        :type s1, s2: str, str
        :rtype: int
        """
        # remove unique chars in both strs first
        s1 = self.remove_unique_chars(s1, set(s2))
        s2 = self.remove_unique_chars(s2, set(s1))

        common_count_1 = self.directed_commonChild(s1, s2)
        common_count_2 = self.directed_commonChild(s2, s1)
        
        return max(common_count_1, common_count_2)
