class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 0 if target <= nums[0] else 1
        else:
            # compare with 
            for i in range(0, len(nums)-1):
                if target <= nums[i]:
                    return i
                else:
                    if target <= nums[i+1]:
                        return i+1
            # compare with last digit
            return len(nums)
