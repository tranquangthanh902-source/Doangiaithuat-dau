class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        closest = nums[0]
        min_dist = abs(nums[0])

        for num in nums:
            dist = abs(num)

            if dist < min_dist or (dist == min_dist and num > closest):
                closest = num
                min_dist = dist

        return closest