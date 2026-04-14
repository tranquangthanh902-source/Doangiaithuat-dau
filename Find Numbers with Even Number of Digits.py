class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in nums:
            s = str(i)
            if len(s) % 2 == 0:
                count += 1
        return count 