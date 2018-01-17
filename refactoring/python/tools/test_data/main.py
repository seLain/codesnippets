class Solution:

    memorized_calc = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        elif n <= 2:
            return n
        else:

            div1 = 0
            if n-1 in self.memorized_calc.keys():
                div1 = self.memorized_calc[n-1]
            else:
                div1 = self.climbStairs(n-1)
                self.memorized_calc[n-1] = div1

            div2 = 0
            if n-2 in self.memorized_calc.keys():
                div2 = self.memorized_calc[n-2]
            else:
                div2 = self.climbStairs(n-2)
                self.memorized_calc[n-2] = div2

            return div1 + div2