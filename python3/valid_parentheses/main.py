class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2:
            return False

        stack = []
        close_bracks = {')':'(', '}':'{', ']':'['}
        for b in s:
            if b not in close_bracks.keys():
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                lead_bracks = stack.pop()
                if lead_bracks != close_bracks[b]:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False