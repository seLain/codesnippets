class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 2:
            return True
        else:
            # deal with first
            if nums[0] > nums[1]:
                nums[0] = nums[1]
                return self.check_nondecreasing(nums)
            # deal with middle
            for i in range(1, n-1):
                if nums[i] < nums[i-1]:
                    if nums[i-1] > nums[i+1]:
                        nums[i-1] = nums[i]
                    elif nums[i-1] <= nums[i+1]:
                        nums[i] = nums[i-1]
                    return self.check_nondecreasing(nums)
            # deal with tail: the tail does not matter
            
            # no violation
            return True

    def check_nondecreasing(self, nums):

        n = len(nums)
        if n < 2:
            return True
        else:
            for i in range(1, n):
                if nums[i] < nums[i-1]:
                    return False
            return True

        





