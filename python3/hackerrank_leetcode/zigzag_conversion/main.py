class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2 or len(s) < 2:
            return s

        total_length = len(s)
        index_diff = 2 * numRows - 2
        merged_strs = ["" for i in range(0, numRows)] # list of merged strings
        merge_flag = 0
        for x in range(0, total_length, index_diff):
            # deal with straight part
            if x + numRows <= total_length:
                for y in range(x, x + numRows):
                    merged_strs[y-x] += s[y]
            else:
                for y in range(x, total_length):
                    merged_strs[y-x] += s[y]
            # deal with slide part
            if x + index_diff <= total_length:
                for y in range(x+numRows, x+index_diff):
                    merged_strs[x+index_diff-y] += s[y]
            else:
                for y in range(x+numRows, total_length):
                    merged_strs[x+index_diff-y] += s[y]

        converted_str = "".join(merged_strs)

        return converted_str