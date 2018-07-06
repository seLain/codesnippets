class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        else:
            recur_str = self.countAndSay(n-1)
            base_char = recur_str[0]
            trans_str_list = []
            counter = 1
            for flag_char in recur_str[1:]:
                if flag_char == base_char:
                    counter += 1
                else:
                    trans_str_list.append(str(counter)+base_char)
                    base_char = flag_char
                    counter = 1
            # deal with flag_char = last char
            trans_str_list.append(str(counter)+base_char)
            
            return ''.join(trans_str_list)