class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        sign = 1
        if x < 0:
        	sign = -1

        r = 0
        n = abs(x)
        while n > 0:
        	m = n % 10
        	n = int(n/10)
        	r = r * 10 + m

        r = r * sign

        if r > 2147483647 or r < -2147483648:
        	return 0

        return r

