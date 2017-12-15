class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) < 1:
            return len(nums)

        remove_flag = 0
        while remove_flag < len(nums):
            if nums[remove_flag] == val:
                nums.pop(remove_flag)
            else:
                remove_flag += 1

        return len(nums)