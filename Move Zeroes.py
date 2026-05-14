class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nonzero, i = 0, 0  # Initialize pointers
        n = len(nums)
        while i < n:
            if nums[i] != 0:
                # Swap non-zero element with the element at the `nonzero` pointer
                nums[i], nums[nonzero] = nums[nonzero], nums[i]
                nonzero += 1  # Move `nonzero` pointer
            i += 1  # Move `i` point