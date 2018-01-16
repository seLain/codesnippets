class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left_to_right = True
        remained_n = n
        forward_steps = 1
        pivot = 1

        while remained_n > 1:
            if left_to_right or remained_n % 2 == 1:
                pivot += forward_steps
            remained_n = remained_n // 2
            forward_steps = forward_steps * 2
            left_to_right = not left_to_right

        return pivot