class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
        	return False

        r = 0
        n = x
        while n > 0:
        	m = n % 10
        	n = int(n/10)
        	r = r * 10 + m

        if r > 2147483647:
        	return False

        if r == x:
        	return True

        return False