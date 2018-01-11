class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return 0

        # find largest and second large
        largest = 0
        largest_index = -1
        second_large = 0
        for i in range(0, len(nums)):
            if nums[i] > largest:
                second_large = largest
                largest = nums[i]
                largest_index = i
            elif second_large < nums[i] <= largest:
                second_large = nums[i]
        # test if largest >= second_large * 2
        if largest >= second_large*2:
            return largest_index
        else:
            return -1
