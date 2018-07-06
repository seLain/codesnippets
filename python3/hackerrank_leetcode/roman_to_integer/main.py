class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        last_number = 0
        value = 0
        for romain_digit in s:
        	current_number = roman_dict[romain_digit]
        	if current_number <= last_number:
        		value += current_number
        	elif current_number > last_number:
        		value = value - last_number + (current_number - last_number)
        	# move the last_number flag
        	last_number = current_number

        return value