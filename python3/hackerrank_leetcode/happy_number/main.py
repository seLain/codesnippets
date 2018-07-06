class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return self.recur_isHappy(n, [])

    def recur_isHappy(self, n, sums):

        if n < 1:
            return False
        elif n == 1:
            return True
        elif n > 2147483647: # uplimit of 32bit integer
            return False
        else:
            new_n = 0
            for digit in [int(d) for d in str(n)]:
                new_n += pow(digit, 2)
            if new_n in sums:
                return False
            else:
                sums.append(new_n)
                return self.recur_isHappy(new_n, sums)