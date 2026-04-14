class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] *= -1
        
        # Bước 2: Những vị trí nào vẫn dương thì index + 1 là số bị thiếu
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
                
        return res