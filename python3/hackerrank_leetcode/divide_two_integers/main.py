import sys

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None

        abs_remainder = abs(dividend)
        abs_divisor = abs(divisor)
        counter = 0
        while abs_remainder >= abs_divisor:
            abs_remainder -= abs_divisor
            counter += 1

        if dividend < 0:
            counter = 0 - counter

        if divisor < 0:
            counter = 0 - counter

        if counter > 2147483647:
            return 2147483647
        elif counter < -2147483648:
            return -2147483648

        return counter