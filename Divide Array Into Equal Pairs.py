class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()  # Sort the array
        for i in range(0, len(nums), 2):
            if nums[i] != nums[i + 1]:  # Check pairs
                return False
        return True


              #pairwise Iteration
class Solution:
    def divideArray(self, nums):
        nums.sort()
        for i in range(1, len(nums), 2):
            if nums[i] != nums[i - 1]:
                return False
        return True