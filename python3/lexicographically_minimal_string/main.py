class Solution:
    def lexicographically_minimal_string(self, a, b):
        """
        :type strs: a, b
        :rtype: str
        """
        a = [ord(x) for x in list(a[::-1])]
        b = [ord(x) for x in list(b[::-1])]
        lms = []
        while len(a) != 0 and len(b) != 0:
            if a[-1] < b[-1]:
                lms.append(a.pop())
            elif a[-1] > b[-1]:
                lms.append(b.pop())
            else:
                s = self.look_forward(a, b)
                flag_char = s.pop()
                lms.append(flag_char)
                # move in later chars which is the same as flag_char
                # in this stack (for efficiency)
                while len(s) > 0 and s[-1] == flag_char:
                    lms.append(s.pop())
                
        if len(a) == 0 and len(b) != 0:
            lms += b[::-1]
        elif len(b) == 0 and len(a) != 0:
            lms += a[::-1]
        
        return ''.join([chr(x) for x in lms])

    def look_forward(self, a, b):
        # find smaller option layer by layer
        for i in range(-1, -min(len(a), len(b)), -1):
            if a[i-1] == b[i-1]:
                continue
            elif a[i-1] < b[i-1]:
                return a
            elif a[i-1] > b[i-1]:
                return b
        # can not find smaller one until the last layer
        if len(a) <= len(b):
            return b
        else:
            return a
