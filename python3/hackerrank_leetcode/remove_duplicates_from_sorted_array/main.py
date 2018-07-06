class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        base_flag = 0
        remove_flag = 1
        while remove_flag < len(nums):
            if nums[base_flag] == nums[remove_flag]:
                nums.pop(remove_flag)
            else:
                base_flag = remove_flag
                remove_flag = base_flag + 1

        return len(nums)